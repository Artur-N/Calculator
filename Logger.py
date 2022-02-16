from datetime import datetime as dt

operation = {
    1: 'Sum',
    2: 'Diff',
    3: 'Div',
    4: 'Mult'
    }

def Complex_log (x, y, oper, res):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};Type: Complex;input: {};{};operation: {};result{}\n'
                    .format(time, x, y, operation[oper], res))

def Rational_log (x, y, oper, res):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};Type: Rational;input: {};{};operation: {};result{}\n'
                    .format(time, x, y, operation[oper], res))
