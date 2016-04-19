import unittest

import cache_requests
from lxml import html
import pypunters


class ScraperTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		cls.http_client = cache_requests.Session()
		cls.html_parser = html.fromstring
		cls.scraper = pypunters.Scraper(cls.http_client, cls.html_parser)

	def check_expected_items(self, expected_items, scraped_items):
		"""Ensure that all items in expected_items are also in scraped_items"""

		for expected_item in expected_items:
			self.assertIn(expected_item, scraped_items)

	def check_unexpected_items(self, expected_items, scraped_items):
		"""Ensure that all items in scraped_items are also in expected_items"""

		for scraped_item in scraped_items:
			self.assertIn(scraped_item, expected_items)