import unittest
import sys
from Calculator.Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.testData = CsvReader("Tests/Data/Addition.csv")

    def test_instantiate_calculator(self):  # tests the instanstiation of the calculator object
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition(self):
        testData = CsvReader("Tests/Data/Addition.csv").data
        for row in testData:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
            pprint(row)


    def test_multiplication(self):
        CsvReader.clear_data(self.testData)
        testData = CsvReader("Tests/Data/Multiplication.csv").data
        for row in testData:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
            pprint(row)


    def test_subtraction(self):
        CsvReader.clear_data(self.testData)
        testData = CsvReader("Tests/Data/Subtraction.csv").data
        for row in testData:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)
            pprint(row)

    def test_square(self):
        CsvReader.clear_data(self.testData)
        testData = CsvReader("Tests/Data/Square.csv").data
        for row in testData:
            result = float(row['Result'])
            self.assertEqual(self.calculator.squaring(row['Value 1']), result)
            pprint(row)

    def test_square_root(self):
        CsvReader.clear_data(self.testData)
        testData = CsvReader("Tests/Data/SquareRoot.csv").data
        for row in testData:
            result = round(float(row['Result']), 8)
            self.assertEqual(self.calculator.sqrt(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)
            pprint(row)

    def test_division(self):
        CsvReader.clear_data(self.testData)
        testData = CsvReader("Tests/Data/Division.csv").data
        for row in testData:
            result = round(float(row['Result']), 9)
            self.assertEqual((self.calculator.divide(row['Value 1'], row['Value 2'])), result)
            self.assertEqual(self.calculator.result, result)
            pprint(row)


if __name__ == '__main__':
    unittest.main()
