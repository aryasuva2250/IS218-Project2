from Statistics.Variance import variance
from Calculator.square_root import Square_Root
def standard_deviation(x):
    result = Square_Root.square_root(variance(x))
    return result