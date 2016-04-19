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

	def check_expected_values(self, expected_values, scraped_values):
		"""Ensure that all key/value pairs in expected_values are also in scraped_values"""

		for key in expected_values:
			self.assertIn(key, scraped_values)
			self.assertEqual(expected_values[key], scraped_values[key])

	def check_unexpected_values(self, expected_values, scraped_values):
		"""Ensure that all keys in scraped_values are also in expected_values"""

		for key in scraped_values:
			self.assertIn(key, expected_values)