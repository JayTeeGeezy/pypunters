from datetime import datetime
import unittest

import cache_requests
from lxml import html
import pypunters


class MeetsTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		
		cls.date = datetime(2016, 2, 1)
		cls.expected_meets = [
			{
				'date':		cls.date,
				'track':	'Kilmore',
				'url':		'/racing-results/victoria/Kilmore/2016-02-01/'
			},
			{
				'date':		cls.date,
				'track':	'Nowra',
				'url':		'/racing-results/new-south-wales/Nowra/2016-02-01/'
			}
		]
		cls.http_client = cache_requests.Session()
		cls.html_parser = html.fromstring
		cls.scraper = pypunters.Scraper(cls.http_client, cls.html_parser)

		cls.scraped_meets = cls.scraper.scrape_meets(cls.date)

	def setUp(self):
		
		self.assertIsInstance(self.scraped_meets, list)

	def test_expected_meets(self):
		"""The scrape_meets method should return a list containing all expected meets"""

		for expected_meet in self.expected_meets:
			self.assertIn(expected_meet, self.scraped_meets)

	def test_unexpected_meets(self):
		"""The scrape_meets method should return a list that does not contain any unexpected meets"""
		
		for scraped_meet in self.scraped_meets:
			self.assertIn(scraped_meet, self.expected_meets)