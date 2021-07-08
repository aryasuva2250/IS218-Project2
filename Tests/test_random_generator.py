import unittest

from RandomGenerator.random_generator import RandomGenerator

class RandomGeneratorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.random_generator = RandomGenerator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.random_generator, RandomGenerator)

    def test_random_num_without_seed(self):
        random_generator = RandomGenerator()
        print(random_generator.random_num(0, 100))

    def test_random_num_with_seed(self):
        random_generator = RandomGenerator()
        r = random_generator.random_seed(0, 100, 10)
        self.assertEqual(random_generator.random_seed(0, 100, 10), r)

    def test_random_list(self):
        random_generator = RandomGenerator()
        r = random_generator.random_list(0, 100, 10, 10)
        #self.assertEqual(random_generator.random_list(0, 100, 10, 5), r)
        return r

if __name__ == '__main__':
    unittest.main()
