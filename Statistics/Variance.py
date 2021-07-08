from Calculator.addition import Addition
from Calculator.division import Division
from Calculator.subtraction import Subtraction
from Calculator.square import Square
from Statistics.Mean import mean

#import statistics
def variance(x):
    '''
    x_mean = mean(x)
    result = sum([Square.square(x - x_mean)  for c in x]) / len(x)
    #result = Division.division(len(x), sum(Square.square((Subtraction.subtraction(x_mean, x)))))
    return result
    '''
    '''
    x_mean = mean(x)
    for value in x:
        numberator1 = Subtraction.subtraction(x_mean, value)
        numerator2 = Square.square(numberator1)
        numerator3 = Addition.addition((numerator2))
        denominator = Subtraction.subtraction(1, (len(x)))
        result = Division.division(denominator, numerator3)
        return result
    '''
    t = sum(x)
    length = len(x)
    s = []
    for value in x:
        s.append(Square.square(value))
    total = sum(s)
    num = Subtraction.subtraction(total, Division.division(t), length)
    den = Subtraction.subtraction(length, 1)
    return round(Division.division(den, num), 2)

    #return statistics.variance(x)
