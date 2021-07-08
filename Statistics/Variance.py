from Calculator.division import Division
from Calculator.subtraction import Subtraction
from Calculator.square import Square
from Statistics.Mean import mean
def variance(x):
    x_mean = mean(x)
    result = sum([Square.square(Subtraction.subtraction(x - x_mean))  for x in x]) / len(x)
    #result = Division.division(len(x), sum(Square.square((Subtraction.subtraction(x_mean, x)))))
    return result
