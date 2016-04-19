from datetime import datetime

from .common import ScraperTest


class MeetsTest(ScraperTest):

	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		
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

		cls.scraped_meets = cls.scraper.scrape_meets(cls.date)

	def setUp(self):
		
		self.assertIsInstance(self.scraped_meets, list)

	def test_expected_meets(self):
		"""The scrape_meets method should return a list containing all expected meets"""

		self.check_expected_items(self.expected_meets, self.scraped_meets)

	def test_unexpected_meets(self):
		"""The scrape_meets method should return a list that does not contain any unexpected meets"""
		
		self.check_unexpected_items(self.expected_meets, self.scraped_meets)