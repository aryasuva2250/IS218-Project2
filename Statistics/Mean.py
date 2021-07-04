from Calculator.addition import addition
from Calculator.division import division

def mean(x):
    val = len(x)
    total = 0
    for num in x:
        total = addition(total, num)
    return division(val, total)