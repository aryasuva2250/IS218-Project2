import unittest
from CsvReader.CsvReader import CsvReader, ClassFactory
from Calculator.Calculator import Calculator
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.Calculator = Calculator()

    def test_addition_reader(self):
        self.csv_reader = CsvReader('Tests/Data/Addition.csv')
        data = self.csv_reader.return_data_as_objects()
        for row in data:
            self.assertEqual(self.Calculator.add(row['Value 1'], row['Value 2']), row['Result'])

    def test_subtraction_reader(self):
        self.csv_reader = CsvReader('Tests/Data/Subtraction.csv')
        data = self.csv_reader.return_data_as_objects()
        for row in data:
            self.assertEqual(self.Calculator.subtract(row['Value 1'], row['Value 2']), row['Result'])

    def test_division_reader(self):
        self.csv_reader = CsvReader('Tests/Data/Division.csv')
        data = self.csv_reader.return_data_as_objects()
        for row in data:
            self.assertEqual(self.Calculator.divide(row['Value 1'], row['Value 2']), row['Result'])

    def test_multiply_reader(self):
        self.csv_reader = CsvReader('Tests/Data/Multiplication.csv')
        data = self.csv_reader.return_data_as_objects()
        for row in data:
            self.assertEqual(self.Calculator.multiply(row['Value 1'], row['Value 2']), row['Result'])

    def test_square_reader(self):
        self.csv_reader = CsvReader('Tests/Data/Square.csv')
        data = self.csv_reader.return_data_as_objects()
        for row in data:
            self.assertEqual(self.Calculator.squaring(row['Value 1'], row['Value 2']), row['Result'])

    def test_square_root_reader(self):
        self.csv_reader = CsvReader('Tests/Data/SquareRoot.csv')
        data = self.csv_reader.return_data_as_objects()
        for row in data:
            self.assertEqual(self.Calculator.sqrt(row['Value 1'], row['Value 2']), row['Result'])
    '''
    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__ )
    '''
if __name__ == '__main__':
    unittest.main()
