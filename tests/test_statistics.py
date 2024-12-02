import unittest
from lib.calculator import Calculator

class TestStatistics(unittest.TestCase):

    def setUp(self):
        """
        Initialisation d'un objet Calculator avant chaque test.
        
        Cette methode est appelee avant chaque test unitaire.
        """
        self.calc = Calculator()

    def test_mean(self):
        self.assertEqual(self.calc.mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(self.calc.mean([10, 20, 30]), 20)
        self.assertEqual(self.calc.mean([1, 1, 1]), 1)

    def test_standard_deviation(self):
        self.assertAlmostEqual(self.calc.standard_deviation([1, 2, 3, 4, 5]), 1.414, places=3)
        self.assertAlmostEqual(self.calc.standard_deviation([1, 1, 1, 1]), 0.0, places=3)
        self.assertAlmostEqual(self.calc.standard_deviation([2, 4, 6, 8]), 2.236, places=3)

    def test_summary_statistics(self):
        stats = self.calc.summary_statistics([1, 2, 3, 4, 5])
        self.assertEqual(stats["mean"], 3)
        self.assertAlmostEqual(stats["standard_deviation"], 1.414, places=3)

if __name__ == '__main__':
    unittest.main()
