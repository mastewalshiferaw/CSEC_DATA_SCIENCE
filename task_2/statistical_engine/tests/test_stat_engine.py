import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):
    def test_even_median(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_median(), 2.5)

    def test_empty_error(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_outliers(self):
        engine = StatEngine([10, 12, 11, 100]) # 100 is clearly an outlier
        outliers = engine.get_outliers(threshold=1)
        self.assertIn(100.0, outliers)

if __name__ == '__main__':
    unittest.main()