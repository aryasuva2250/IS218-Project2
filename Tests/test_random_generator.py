import unittest

from RandomGenerator import random_generator

class RandomGeneratorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.random_generator = random_generator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.random_generator, random_generator)

    def test_random_num_without_seed(self):
        random_generator = self.random_generator()
        print(random_generator.random_num(self, 0, 100))

    def test_random_num_with_seed(self):
        random_generator = self.random_generator()
        r = random_generator.random_seed(self, 0, 100, 10)
        self.assertEqual(random_generator.random_seed(self, 0, 100, 10), r)

    def test_random_list(self):
        random_generator = self.random_generator()
        r = random_generator.random_list(self, 0, 100, 10, 10)
        self.assertEqual(random_generator.random_list(self, 0, 100, 10, 5), r)

if __name__ == '__main__':
    unittest.main()
