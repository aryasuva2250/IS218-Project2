from Calculator.addition import Addition
from Calculator.subtraction import Subtraction
from Calculator.division import Division
from Calculator.square import Square
from Calculator.square_root import Square_Root
from Calculator.multiplication import Multiplication


class Calculator:

    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = Addition.addition(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Multiplication.multiplication(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Subtraction.subtraction(a, b)
        return self.result

    def squaring(self, a):
        self.result = Square.square(a)
        return self.result

    def sqrt(self, a):
        self.result = Square_Root.square_root(float(a))
        return self.result

    def divide(self, a, b):
        self.result = Division.division(a, b)
        return self.result

