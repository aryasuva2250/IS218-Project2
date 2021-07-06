import unittest
#from numpy.random import seed
#from numpy.random import randint
from Calculator.Calculator import Calculator
from RandomGenerator.random_generator import RandomGenerator
from Statistics.Statistics import Statistics
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Standard_Deviation import standard_deviation
from Statistics.Variance import variance
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testing = [1, 2, 3, 4, 5]
        self.testing1 = [2, 2, 4, 6, 9, 1]
        self.testing3 = [1, 10, 5, 4, 5]
        self.testing4 = [1, 8, 6,]
        #seed(5)
        #self.testData = randint(0, 10, 20)
        #self.statistics = Statistics()

    #def test_instantiate_calculator(self):
     #   self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        self.assertEqual(3, mean.mean(self.testing))

    def test_median_calculator(self):
        self.assertEqual(3, median.median(self.testing1))

    def test_mode_calculator(self):
        self.assertEqual(3, mode.mode(self.testing2))

    def test_standard_deviation_calculator(self):
        self.assertEqual(3, standard_deviation.standard_deviation(self.testing3))

    def test_variance_calculator(self):
        self.assertEqual(2, variance.variance(self.testing4))


if __name__ == '__main__':
    unittest.main()