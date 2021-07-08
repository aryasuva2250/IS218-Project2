from Calculator.addition import Addition
from Calculator.division import Division

def mean(x):
    val = len(x)
    total = 0
    for num in x:
        total = Addition.addition(total, num)
    return Division.division(val, total)