import view

op = view.in_operation()
operation = {
    1: lambda x,y: x+y,
    2: lambda x,y: x-y,
    3: lambda x,y: x/y,
    4: lambda x,y: x*y
    }

def calculation (x, y, oper = operation[op]):
    return oper(x,y)

def input():
    x = view.in_complex('1')
    y = view.in_complex('2')
    return calculation(x,y)