from datetime import datetime

from .common import ScraperTest


class TrainersTest(ScraperTest):

	@classmethod
	def setUpClass(cls):
		super().setUpClass()

		cls.url = '/trainers/Scott-McIntosh_1010/'
		cls.expected_values = {
			'url':	cls.url,
			'name':	'Scott McIntosh'
		}

		cls.scraped_values = cls.scraper.scrape_trainer(cls.url)

	def setUp(self):

		self.assertIsInstance(self.scraped_values, dict)

	def test_expected_values(self):
		"""The scrape_trainer method should return a dictionary containing all expected values"""

		self.check_expected_values(self.expected_values, self.scraped_values)