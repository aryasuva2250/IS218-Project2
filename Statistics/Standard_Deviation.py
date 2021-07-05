from Statistics.Variance import variance
from Calculator.square_root import square_root
def standard_deviation(x):
    result = square_root(variance(x))
    return result