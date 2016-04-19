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

	def scrape_meets(self, date):
		"""Scrape a list of meets occurring on the specified date"""

		meets = []

		response = self.http_client.get('https://www.punters.com.au/racing-results/{date:%Y-%m-%d}/'.format(date=date))
		response.raise_for_status()
		html = self.html_parser(response.text)
		if html is not None:
			
			for link in html.cssselect('a.label-link'):
				meets.append({
					'date':		date,
					'track':	link.text_content().strip(),
					'url':		link.get('href')
					})

		return meets