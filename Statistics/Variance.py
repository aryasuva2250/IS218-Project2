from Calculator.division import division
from Calculator.subtraction import subtraction
from Calculator.square import square
from Statistics.Mean import mean
def variance(x):
    x_mean = mean(x)
    result = division(len(x), sum(square((subtraction(x_mean, x)))))
    return result
