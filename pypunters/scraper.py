from datetime import datetime
import re

from .html_utils import *


class Scraper:
	"""Web scraper for www.punters.com.au"""

	def __init__(self, http_client, html_parser):
		"""Initialize a new scraper

		http_client must be an object that conforms to the Requests API, supporting calls such as the following:
		response = http_client.get(url)
		response.raise_for_status()
		content = response.text

		html_parser must be a callable that conforms to the lxml.html.fromstring signature, supporting calls such as the following:
		html = html_parser(content)
		"""

		self.http_client = http_client
		self.html_parser = html_parser

		self.scrape_horse = self.scrape_jockey = self.scrape_trainer = self.scrape_profile

	def get_html(self, url, url_root='https://www.punters.com.au/', url_separator='/'):
		"""Get the root HTML element from the specified URL"""

		if not url.startswith(url_root):
			if not url.startswith(url_separator) and not url_root.endswith(url_separator):
				url = url_separator + url
			url = url_root + url

		response = self.http_client.get(url)
		response.raise_for_status()

		return self.html_parser(response.text)

	def fix_profile_url(self, url):
		"""Remove apprentice indicators from profile URLs"""

		return re.sub('\-\%28a\d*\.?\d*\%29', '', url)

	def scrape_meets(self, date):
		"""Scrape a list of meets occurring on the specified date"""

		meets = []

		html = self.get_html('https://www.punters.com.au/racing-results/{date:%Y-%m-%d}/'.format(date=date))
		if html is not None:
			
			for link in html.cssselect('a.label-link'):
				link_href = link.get('href')
				if re.search('/(australian-capital-territory|new-south-wales|northern-territory|queensland|south-australia|tasmania|victoria|western-australia)/.*/{date:%Y-%m-%d}'.format(date=date), link_href):
					
					meets.append({
						'date':		date,
						'track':	link.text_content().strip(),
						'url':		link_href
						})

		return meets

	def scrape_races(self, meet):
		"""Scrape a list of races occurring at the specified meet"""

		def get_prize_money(element):
			prize_money = None
			prize_money_groups = get_child_match_groups(element, 'span.capitalize', '\$(\d+\.?\d*)([kKmM])\:', index=0)
			if prize_money_groups is not None and len(prize_money_groups) > 0:
				try:
					prize_money = float(prize_money_groups[0])
					if len(prize_money_groups) > 1:
						multiplier = prize_money_groups[1].upper()
						if multiplier == 'K':
							prize_money *= 1000
						elif multiplier == 'M':
							prize_money *= 1000000
				except ValueError:
					pass
			return prize_money

		def get_start_time(element):
			try:
				return datetime.fromtimestamp(parse_attribute(header, 'abbr.timestamp', 'data-utime', int))
			except ValueError:
				return None

		races = []

		html = self.get_html(meet['url'])
		if html is not None:
			
			for table in html.cssselect('table.results-table'):
				header = get_child(table, 'thead tr th')
				if header is not None:

					race = {
						'number':			parse_child_match_group(header, 'b.capitalize', 'Race (\d+)', int),
						'distance':			parse_attribute(header, 'span.distance abbr.conversion[data-type=distance]', 'data-value', int),
						'prize_money':		get_prize_money(header),
						'track_condition':	get_child_text(header, 'span.capitalize', index=1),
						'start_time':		get_start_time(header),
						'url':				get_attribute(header, 'a', 'href'),
						'entry_conditions':	[],
						'track_circ':		None,
						'track_straight':	None,
						'track_rail':		None
						}

					html2 = self.get_html(race['url'])
					if html2 is not None:
						
						race['entry_conditions'] = [span.text_content().replace('.', '').strip() for span in html2.cssselect('div.event-details span.entry-conditions-text span')]

						detail_spans = html2.cssselect('div.event-details-bottom div span')
						for index in range(0, len(detail_spans) - 1, 2):
							key = detail_spans[index].text_content().strip().lower()

							if key in ('circ', 'straight'):
								race['track_' + key] = parse_attribute(detail_spans[index + 1], 'abbr.conversion[data-type=distance]', 'data-value', int)

							elif key == 'rail':
								race['track_rail'] = detail_spans[index + 1].text_content().strip()

					races.append(race)

		return races

	def scrape_runners(self, race):
		"""Scrape a list of runners competing in the specified race"""
		
		runners = []

		html = self.get_html(race['url'])
		if html is not None:
			
			for row in html.cssselect('table.form-overview tbody tr'):
				row_class = row.get('class')
				if row_class is None or 'scratched' not in row_class:

					runner = {
						'number':				parse_attribute(row, None, 'data-runner-number', int),
						'horse_url':			None,
						'horse_has_blinkers':	get_child(row, 'div.has-blinkers') is not None,
						'jockey_url':			None,
						'jockey_is_apprentice':	False,
						'jockey_claiming':		0.0,
						'trainer_url':			None,
						'weight':				parse_attribute(row, None, 'data-weight', float),
						'barrier':				parse_attribute(row, None, 'data-barrier', float)
						}

					for link in row.cssselect('a'):
						link_href = link.get('href')
						for key in ('horse', 'jockey', 'trainer'):
							if link_href.startswith('/{key}s/'.format(key=key)):
								runner[key + '_url'] = self.fix_profile_url(link_href)
								break

					apprentice_text = get_child_text(row, 'span.timeSince')
					if apprentice_text is not None:
						runner['jockey_is_apprentice'] = True
						apprentice_match = re.search('\(a(\d+\.?\d*)\)', apprentice_text)
						if apprentice_match is not None:
							apprentice_groups = apprentice_match.groups()
							if apprentice_groups is not None and len(apprentice_groups) > 0:
								try:
									runner['jockey_claiming'] = float(apprentice_groups[0])
								except ValueError:
									pass

					runners.append(runner)

		return runners

	def scrape_profile(self, url):
		"""Scrape a single profile's profile from the specified URL"""

		def get_name(element):
			name = get_child_text(element, 'h1')
			if name is not None:
				inner_text = get_child_text(element, 'h1 span')
				if inner_text is not None:
					name = name.replace(inner_text, '').strip()
				name = re.sub('\(a\d*\.?\d*\)', '', name).strip()
			return name

		html = self.get_html(url)
		if html is not None:
			
			profile = {
				'url':	url,
				'name':	get_name(html)
			}

			for row in html.cssselect('div.moduleItem table tr'):
				label = get_child_text(row, 'th')
				if label is not None:
					label = label.replace(':', '').strip().lower()

					if label == 'profile':
						profile_groups = get_child_match_groups(row, 'td', 'year old (.*) (.*)')
						if profile_groups is not None and len(profile_groups) > 0:
							profile['sex'] = profile_groups[-1]
							if len(profile_groups) > 1:
								profile['colour'] = profile_groups[0]

					elif label == 'pedigree':
						pedigree_groups = get_child_match_groups(row, 'td', '(.*) x (.*)')
						if pedigree_groups is not None and len(pedigree_groups) > 0:
							profile['dam'] = pedigree_groups[-1]
							if len(pedigree_groups) > 1:
								profile['sire'] = pedigree_groups[0]

					elif label == 'country':
						profile['country'] = get_child_text(row, 'td')

					elif label == 'foaled':
						try:
							profile['foaled'] = datetime.strptime(get_child_text(row, 'td'), '%d/%m/%Y')
						except ValueError:
							pass

			return profile

	def scrape_performances(self, url):
		"""Scrape a list of performances from the specified URL"""

		def parse_date(text):
			if text is not None:
				try:
					return datetime.strptime(text, '%d-%b-%y')
				except ValueError:
					return None

		def parse_time(text):
			if text is not None:
				try:
					time = None
					time_parts = text.split(':')
					if len(time_parts) > 0:
						time = float(time_parts[-1])
						if len(time_parts) > 1:
							time += int(time_parts[0]) * 60
						time = round(time, 2)
					return time
				except ValueError:
					return None

		performances = []

		html = self.get_html(url)
		if html is not None:
			
			for ul in html.cssselect('ul.timeline'):
				if not 'TRIAL' in ul.text_content():
					result_text = get_child_text(ul, 'span.formSummaryPosition')
					if result_text is not None and result_text != 'Abn':

						performance = {
							'result':				parse_child_text(ul, 'span.formSummaryPosition', int),
							'starters':				parse_child_text(ul, 'span.starters', int),
							'track':				get_child_text(ul, 'span.simlight'),
							'date':					parse_child_text(ul, 'span.date', parse_date),
							'distance':				parse_attribute(ul, 'span.dist abbr.conversion[data-type=distance]', 'data-value', int),
							'track_condition':		get_child_text(ul, 'span.badge'),
							'runner_prize_money':	None,
							'race_prize_money':		None,
							'barrier':				parse_child_text(ul, 'span.barrier', int),
							'winning_time':			parse_child_text(ul, 'span.time', parse_time),
							'starting_price':		parse_child_match_group(ul, 'span.sp', '\$(\d+\.?\d*)', float),
							'horse_url':			None,
							'jockey_url':			None,
							'weight':				None,
							'carried':				None,
							'lengths':				0.00
						}

						prize_monies = parse_attributes(ul, 'abbr.conversion[data-type=currency]', 'data-value', float)
						if len(prize_monies) > 0:
							performance['race_prize_money'] = prize_monies[-1]
							if len(prize_monies) > 1:
								performance['runner_prize_money'] = prize_monies[0]

						placed_span = get_child(ul, 'span.timeline-right.placed')
						if placed_span is not None:

							for link in placed_span.cssselect('a'):
								link_href = link.get('href')
								for key in ('horse', 'jockey'):
									if link_href.startswith('/{key}s/'.format(key=key)):
										performance[key + '_url'] = self.fix_profile_url(link_href)
										break

							weights = parse_attributes(placed_span, 'abbr.conversion[data-type=weight]', 'data-value', float)
							if len(weights) > 0:
								performance['weight'] = performance['carried'] = weights[-1]
								if len(weights) > 1:
									performance['weight'] = weights[0]

							lengths_match = re.search('\)\W+(\d+\.?\d*)L', placed_span.text_content())
							if lengths_match is not None:
								lengths_groups = lengths_match.groups()
								if lengths_groups is not None and len(lengths_groups) > 0:
									try:
										performance['lengths'] = float(lengths_groups[0])
									except ValueError:
										pass

						performances.append(performance)

		return performances