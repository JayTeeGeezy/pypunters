from datetime import datetime

from .common import ScraperTest


class PerformancesTest(ScraperTest):

	@classmethod
	def setUpClass(cls):
		super().setUpClass()

		cls.url = '/horses/Tycoon-Tony_395471/'
		cls.expected_performances = [
			{
				'result':				3,
				'starters':				12,
				'track':				'Echuca',
				'date':					datetime(2016, 4, 10),
				'distance':				1209,
				'track_condition':		'Good 4',
				'runner_prize_money':	1600.00,
				'race_prize_money':		20000.00,
				'barrier':				15,
				'winning_time':			73.2,
				'starting_price':		6.50,
				'horse_url':			'/horses/Tycoon-Tony_395471/',
				'jockey_url':			'/jockeys/Mark-Pegus_980/',
				'weight':				60.5,
				'carried':				60.5,
				'lengths':				0.30
			},
			{
				'result':				3,
				'starters':				4,
				'track':				'Yarra Valley',
				'date':					datetime(2016, 3, 20),
				'distance':				1200,
				'track_condition':		'Heavy 9',
				'runner_prize_money':	2000.00,
				'race_prize_money':		25000.00,
				'barrier':				4,
				'winning_time':			76.55,
				'starting_price':		2.10,
				'horse_url':			'/horses/Tycoon-Tony_395471/',
				'jockey_url':			'/jockeys/Ben-Allen_9146/',
				'weight':				60.5,
				'carried':				59.0,
				'lengths':				2.95
			},
			{
				'result':				6,
				'starters':				11,
				'track':				'Sandown Hillside',
				'date':					datetime(2016, 2, 17),
				'distance':				1300,
				'track_condition':		'Soft 5',
				'runner_prize_money':	700.00,
				'race_prize_money':		35000.00,
				'barrier':				4,
				'winning_time':			79.18,
				'starting_price':		9.00,
				'horse_url':			'/horses/Tycoon-Tony_395471/',
				'jockey_url':			'/jockeys/Harry-Coffey_3109/',
				'weight':				61.0,
				'carried':				59.5,
				'lengths':				4.35
			},
			{
				'result':				2,
				'starters':				8,
				'track':				'Kilmore',
				'date':					datetime(2016, 2, 1),
				'distance':				1100,
				'track_condition':		'Good 4',
				'runner_prize_money':	3400.00,
				'race_prize_money':		20000.00,
				'barrier':				2,
				'winning_time':			63.6,
				'starting_price':		4.00,
				'horse_url':			'/horses/Tycoon-Tony_395471/',
				'jockey_url':			'/jockeys/Ben-E-Thompson_2143/',
				'weight':				61.0,
				'carried':				59.5,
				'lengths':				0.10
			},
			{
				'result':				9,
				'starters':				12,
				'track':				'Wangaratta',
				'date':					datetime(2016, 1, 21),
				'distance':				1300,
				'track_condition':		'Good 4',
				'runner_prize_money':	500.00,
				'race_prize_money':		20000.00,
				'barrier':				12,
				'winning_time':			77.55,
				'starting_price':		8.00,
				'horse_url':			'/horses/Tycoon-Tony_395471/',
				'jockey_url':			'/jockeys/Mitchell-Aitken_9402/',
				'weight':				61.0,
				'carried':				58.0,
				'lengths':				5.25
			},
			{
				'result':				1,
				'starters':				14,
				'track':				'Wangaratta',
				'date':					datetime(2016, 1, 4),
				'distance':				1170,
				'track_condition':		'Soft 5',
				'runner_prize_money':	11000.00,
				'race_prize_money':		20000.00,
				'barrier':				5,
				'winning_time':			68.51,
				'starting_price':		10.00,
				'horse_url':			'/horses/Tycoon-Tony_395471/',
				'jockey_url':			'/jockeys/Ben-E-Thompson_2143/',
				'weight':				60.0,
				'carried':				58.5,
				'lengths':				0.00
			},
			{
				'result':				5,
				'starters':				11,
				'track':				'Echuca',
				'date':					datetime(2015, 9, 25),
				'distance':				1100,
				'track_condition':		'Good 4',
				'runner_prize_money':	600.00,
				'race_prize_money':		20000.00,
				'barrier':				1,
				'winning_time':			64.42,
				'starting_price':		7.00,
				'horse_url':			'/horses/Tycoon-Tony_395471/',
				'jockey_url':			'/jockeys/Jason-Collins_2265/',
				'weight':				59.0,
				'carried':				57.0,
				'lengths':				2.80
			},
			{
				'result':				1,
				'starters':				13,
				'track':				'Echuca',
				'date':					datetime(2015, 9, 5),
				'distance':				1200,
				'track_condition':		'Good 4',
				'runner_prize_money':	13000.00,
				'race_prize_money':		20000.00,
				'barrier':				12,
				'winning_time':			72.04,
				'starting_price':		19.00,
				'horse_url':			'/horses/Tycoon-Tony_395471/',
				'jockey_url':			'/jockeys/Jason-Collins_2265/',
				'weight':				58.5,
				'carried':				56.5,
				'lengths':				0.00
			},
			{
				'result':				4,
				'starters':				14,
				'track':				'Echuca',
				'date':					datetime(2015, 8, 17),
				'distance':				1400,
				'track_condition':		'Good 4',
				'runner_prize_money':	900.00,
				'race_prize_money':		20000.00,
				'barrier':				6,
				'winning_time':			85.74,
				'starting_price':		5.00,
				'horse_url':			'/horses/Tycoon-Tony_395471/',
				'jockey_url':			'/jockeys/Jason-Benbow_690/',
				'weight':				58.5,
				'carried':				58.5,
				'lengths':				5.25
			},
			{
				'result':				3,
				'starters':				11,
				'track':				'Wodonga',
				'date':					datetime(2015, 7, 29),
				'distance':				1100,
				'track_condition':		'Heavy 9',
				'runner_prize_money':	1200.00,
				'race_prize_money':		15000.00,
				'barrier':				15,
				'winning_time':			67.96,
				'starting_price':		21.00,
				'horse_url':			'/horses/Tycoon-Tony_395471/',
				'jockey_url':			'/jockeys/Jason-Benbow_690/',
				'weight':				58.5,
				'carried':				58.5,
				'lengths':				4.50
			}
		]

		cls.scraped_performances = cls.scraper.scrape_performances(cls.url)

	def setUp(self):

		self.assertIsInstance(self.scraped_performances, list)

	def test_expected_performances(self):
		"""The scrape_performances method should return a list containing all expected performances"""

		self.check_expected_items(self.expected_performances, self.scraped_performances)