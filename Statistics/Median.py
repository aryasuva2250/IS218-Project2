#from Calculator.division import Division
#from Calculator.addition import Addition
#from Calculator.subtraction import subtraction
def median(x):
    x.sort()
    l = len(x)
    if((l % 2) == 0):
        result = ((x[l // 2]) + (x[l // 2]) - 1) // 2
        #result = division(2, (addition(((x[division(2, l)]), subtraction(2, x[division(2, 1)])))))
        return result
        #m1 = x[division(2, l)]
        #m2 = x[subtraction(1, division(l, 2))]
        #result = division(2, (addition(m1, m2)))
    else:
        result = x[(l // 2)]
        return result