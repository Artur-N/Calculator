from datetime import datetime as dt
from time import time

def Complex_log (data, oper, res):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};input complex_digits;{};operation;{};result{}\n'
                    .format(time, data, oper, res))

def Rational_log (data, oper, res):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};input complex_digits;{};operation;{};result{}\n'
                    .format(time, data, oper, res))
