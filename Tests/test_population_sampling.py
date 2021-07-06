import unittest

from RandomGenerator import random_generator
from PopulationsSampling import population_sampling

class PopulationSamplingTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.randomGenerator = random_generator()
        self.populationSampling = population_sampling()

    def test_instantiate_random_generator(self):
        self.assertIsInstance(self.randomGenerator, random_generator)

    def test_instantiate_population_sampling(self):
        self.assertIsInstance(self.populationSampling, population_sampling)

    def test_simple_random_sampling(self):
        testing = self.randomGenerator.random_list(self, 0, 15, 50, 2)
        result = self.populationSampling.simple_random_sampling(self, testing, 10, 5)
        self.assertEqual(self.populationSampling.simple_random_sampling(self, testing, 10, 5), result)
        testing.clear()

    def test_confidence_interval(self):
        testing = [5, 6, 3, 5, 1, 3, 7, 3]
        self.assertEqual(self.populationSampling.confidence_interval(self, testing), [6.5435, 3.675])
        testing.clear()

    def test_margin_error(self):
        testing = [5, 6, 3, 5, 1, 3, 7, 3]
        self.assertEqual(round(self.populationSampling.margin_error(self, testing), 6), 1.83452)
        testing.clear()

if __name__ == '__main__':
    unittest.main()