from datetime import datetime

from .common import ScraperTest


class RunnersTest(ScraperTest):

	@classmethod
	def setUpClass(cls):
		super().setUpClass()

		cls.race = {
			'number':			5,
			'distance':			1100,
			'prize_money':		20000.00,
			'track_condition':	'Good 4',
			'start_time':		datetime(2016, 2, 1, 15, 32),
			'url':				'/form-guide/Kilmore_69146/www.kilmoreracingclub.com.au-BM64-Handicap_411196/',
			'entry_conditions':	[
				'No age restriction',
				'BenchMark 64',
				'No sex restriction',
				'Handicap'
			],
			'track_circ':		1735,
			'track_straight':	320,
			'track_rail':		'True Entire Circuit'
		}
		cls.expected_runners = [
			{
				'number':				1,
				'horse_url':			'/horses/Tycoon-Tony_395471/',
				'horse_has_blinkers':	False,
				'jockey_url':			'/jockeys/Ben-E-Thompson_2143/',
				'jockey_is_apprentice':	True,
				'jockey_claiming':		1.5,
				'trainer_url':			'/trainers/Scott-McIntosh_1010/',
				'weight':				61.0,
				'barrier':				2
			},
			{
				'number':				2,
				'horse_url':			'/horses/Chima_325128/',
				'horse_has_blinkers':	False,
				'jockey_url':			'/jockeys/Cory-Parish_2656/',
				'jockey_is_apprentice':	False,
				'jockey_claiming':		0.0,
				'trainer_url':			'/trainers/David-Hayes-and-Tom-Dabernig_897/',
				'weight':				58.5,
				'barrier':				7
			},
			{
				'number':				3,
				'horse_url':			'/horses/Thisgoingsomewhere_214653/',
				'horse_has_blinkers':	True,
				'jockey_url':			'/jockeys/Jarrod-Fry_686/',
				'jockey_is_apprentice':	False,
				'jockey_claiming':		0.0,
				'trainer_url':			'/trainers/John-and-Chris-Ledger_938/',
				'weight':				58.0,
				'barrier':				5
			},
			{
				'number':				4,
				'horse_url':			'/horses/Azzcool_158971/',
				'horse_has_blinkers':	False,
				'jockey_url':			'/jockeys/Chris-Symons_291/',
				'jockey_is_apprentice':	False,
				'jockey_claiming':		0.0,
				'trainer_url':			'/trainers/Alexander-Rae_13641/',
				'weight':				57.5,
				'barrier':				4
			},
			{
				'number':				6,
				'horse_url':			'/horses/Love-And-Lies_315909/',
				'horse_has_blinkers':	False,
				'jockey_url':			'/jockeys/Rebecca-Williams_2263/',
				'jockey_is_apprentice':	True,
				'jockey_claiming':		1.5,
				'trainer_url':			'/trainers/Jennifer-Williams_4610/',
				'weight':				57.0,
				'barrier':				10
			},
			{
				'number':				7,
				'horse_url':			'/horses/Our-Hussey_81386/',
				'horse_has_blinkers':	True,
				'jockey_url':			'/jockeys/Mitchell-Aitken_9402/',
				'jockey_is_apprentice':	True,
				'jockey_claiming':		3.0,
				'trainer_url':			'/trainers/Russell-Green_8566/',
				'weight':				57.0,
				'barrier':				3
			},
			{
				'number':				8,
				'horse_url':			'/horses/Aglaia_316893/',
				'horse_has_blinkers':	True,
				'jockey_url':			'/jockeys/Brandon-Stockdale_8506/',
				'jockey_is_apprentice':	True,
				'jockey_claiming':		1.5,
				'trainer_url':			'/trainers/Mark-Riley_841/',
				'weight':				56.5,
				'barrier':				9
			},
			{
				'number':				10,
				'horse_url':			'/horses/Sullivan-Bay_322748/',
				'horse_has_blinkers':	False,
				'jockey_url':			'/jockeys/Jye-McNeil_3183/',
				'jockey_is_apprentice':	False,
				'jockey_claiming':		0.0,
				'trainer_url':			'/trainers/David-Hayes-and-Tom-Dabernig_897/',
				'weight':				55.5,
				'barrier':				1
			}
		]

		cls.scraped_runners = cls.scraper.scrape_runners(cls.race)

	def setUp(self):

		self.assertIsInstance(self.scraped_runners, list)

	def test_expected_runners(self):
		"""The scrape_runners method should return a list containing all expected runners"""

		self.check_expected_items(self.expected_runners, self.scraped_runners)

	def test_unexpected_runners(self):
		"""The scrape_runners method should return a list that does not contain any unexpected runners"""

		self.check_unexpected_items(self.expected_runners, self.scraped_runners)