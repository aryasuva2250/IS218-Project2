import unittest
from CsvReader.CsvReader import CsvReader, ClassFactory
from Calculator.Calculator import Calculator
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.Calculator = Calculator()

    def test_instantiate_calculator(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_addition(self):
        self.assertEqual(self.Calculator.add(2, 2), 4)
        self.assertEqual(self.Calculator.result, 4)

    def test_subtraction(self):
        self.assertEqual(self.Calculator.subtract(2, 2), 0)
        self.assertEqual(self.Calculator.result, 0)

    def test_multiplication(self):
        self.assertEqual(self.Calculator.multiply(2, 2), 4)
        self.assertEqual(self.Calculator.result, 4)

    def test_division(self):
        self.assertEqual(self.Calculator.divide(2, 2), 1)
        self.assertEqual(self.Calculator.result, 1)
        try:
            self.Calculator.divide(1, 1)
        except IndexError:
            print('DivideByZeroError')

    def test_square(self):
        self.assertEqual(self.Calculator.squaring(2), 4)
        self.assertEqual(self.Calculator.result, 4)

    def test_square_root(self):
        self.assertEqual(self.Calculator.sqrt(4), 2)
        self.assertEqual(self.Calculator.result, 2)
    '''
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
            self.assertEqual(self.Calculator.squaring(row['Value 1']), row['Result'])

    def test_square_root_reader(self):
        self.csv_reader = CsvReader('Tests/Data/SquareRoot.csv')
        data = self.csv_reader.return_data_as_objects()
        for row in data:
            self.assertEqual(self.Calculator.sqrt(row['Value 1']), row['Result'])
    '''
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
