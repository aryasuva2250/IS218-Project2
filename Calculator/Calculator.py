from Calculator.addition import addition
from Calculator.multiplication import multiplication
from Calculator.subtraction import subtraction
from Calculator.division import division
from Calculator.square import square
from Calculator.square_root import square_root

class Calculator:

    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def squaring(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = square_root(float(a))
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

