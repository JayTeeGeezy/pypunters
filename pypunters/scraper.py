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

	def get_html(self, url, url_root='https://www.punters.com.au/', url_separator='/'):
		"""Get the root HTML element from the specified URL"""

		if not url.startswith(url_root):
			if not url.startswith(url_separator) and not url_root.endswith(url_separator):
				url = url_separator + url
			url = url_root + url

		response = self.http_client.get(url)
		response.raise_for_status()

		return self.html_parser(response.text)

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
						'url':				get_attribute(header, 'a', 'href')
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