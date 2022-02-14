
import view as v
import Logger as log
import converter as conv

"""
Шаг 1 - получить числа - из будущего конвертера
"""
x = conv.get_value()
y = conv.get_value()


"""
Шаг 2  - Вычислить
"""
op = v.in_operation()

def calculation (x, y, op):
    calc = {
        1: lambda x, y: x + y,
        2: lambda x, y: x - y,
        3: lambda x, y: x / y,
        4: lambda x, y: x * y,
        }
    res = calc[op](x, y)
    return res

result = calculation(x, y, op)
print(type(result))
print(result)

"""
Шаг 4 - Отправить аргументы, операцию и результат в логгер - нужен конвертер
"""
if type(result) == 'complex':
    print('it is complex')
elif type(result) == 'float':
    print('it is real')
