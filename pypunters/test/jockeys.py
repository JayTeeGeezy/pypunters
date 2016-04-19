from datetime import datetime

from .common import ScraperTest


class JockeysTest(ScraperTest):

	@classmethod
	def setUpClass(cls):
		super().setUpClass()

		cls.url = '/jockeys/Ben-E-Thompson_2143/'
		cls.expected_values = {
			'url':	cls.url,
			'name':	'Ben E Thompson'
		}

		cls.scraped_values = cls.scraper.scrape_jockey(cls.url)

	def setUp(self):

		self.assertIsInstance(self.scraped_values, dict)

	def test_expected_values(self):
		"""The scrape_jockey method should return a dictionary containing all expected values"""

		self.check_expected_values(self.expected_values, self.scraped_values)