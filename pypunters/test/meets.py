from datetime import datetime
import unittest

import cache_requests
from lxml import html
import pypunters


class MeetsTest(unittest.TestCase):

	def test_expected_meets(self):
		"""The scrape_meets method should return a list containing all expected meets"""

		date = datetime(2016, 2, 1)
		expected_meets = [
			{
				'date':		date,
				'track':	'Kilmore',
				'url':		'/racing-results/victoria/Kilmore/2016-02-01/'
			},
			{
				'date':		date,
				'track':	'Nowra',
				'url':		'/racing-results/new-south-wales/Nowra/2016-02-01/'
			}
		]
		http_client = cache_requests.Session()
		html_parser = html.fromstring
		scraper = pypunters.Scraper(http_client, html_parser)

		scraped_meets = scraper.scrape_meets(date)

		self.assertIsInstance(scraped_meets, list)
		for expected_meet in expected_meets:
			self.assertIn(expected_meet, scraped_meets)