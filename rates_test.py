import rates
import unittest


class TestDailyRates(unittest.TestCase):

  def test_get_daily_rates(self):
    r = rates.get_daily_rates("catcoin", 3)
    self.assertEqual(r, [2.0]*3)


if __name__ == "__main__":
    unittest.main()
