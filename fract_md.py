import view
import Logger as log

operation = {
    1: lambda x,y: x+y,
    2: lambda x,y: x-y,
    3: lambda x,y: x/y,
    4: lambda x,y: x*y
    }

def calculation (x, y, op):
    result = operation[op](x,y)
    log.Rational_log(x,y,op,result)
    return result

def input(op):
    x = view.in_fraction('1')
    y = view.in_fraction('2')
    return calculation(x,y,op)