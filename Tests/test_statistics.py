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
        '''
        self.testing = [1, 2, 3, 4, 5]
        self.testing1 = [2, 2, 4, 6, 9, 1]
        self.testing3 = [1, 10, 5, 4, 5]
        self.testing4 = [1, 8, 6,]
        '''
        #seed(5)
        #self.testData = randint(0, 10, 20)
        self.statistics = Statistics(Calculator)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        statistics = Statistics()
        random_generator = RandomGenerator()
        testing = random_generator.random_list(self, 0, 100, 5, 4)
        mean = statistics.mean(testing)
        self.assertEqual(statistics.mean(testing), mean)
        self.assertEqual(statistics.result, mean)
        testing.clear()

    def test_median_calculator(self):
        statistics = Statistics()
        random_generator = RandomGenerator()
        testing = random_generator.random_list(self, 0, 100, 5, 4)
        median = statistics.median(testing)
        self.assertEqual(statistics.median(testing), median)
        self.assertEqual(statistics.result, median)
        testing.clear()

    def test_mode_calculator(self):
        statistics = Statistics()
        random_generator = RandomGenerator()
        testing = random_generator.random_list(self, 0, 100, 5, 4)
        mode = statistics.mode(testing)
        self.assertEqual(statistics.mode(testing), mode)
        self.assertEqual(statistics.result, mode)
        testing.clear()

    def test_standard_deviation_calculator(self):
        statistics = Statistics()
        random_generator = RandomGenerator()
        testing = random_generator.random_list(self, 0, 100, 5, 4)
        standard_deviation = statistics.standard_deviation(testing)
        self.assertEqual(statistics.standard_deviation(testing), standard_deviation)
        self.assertEqual(statistics.result, standard_deviation)
        testing.clear()

    def test_variance_calculator(self):
        statistics = Statistics()
        random_generator = RandomGenerator()
        testing = random_generator.random_list(self, 0, 100, 5, 4)
        variance = statistics.variance(testing)
        self.assertEqual(statistics.variance(testing), variance)
        self.assertEqual(statistics.result, variance)
        testing.clear()


if __name__ == '__main__':
    unittest.main()