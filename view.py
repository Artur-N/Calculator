from fractions import Fraction
import controller as ctrl
def in_operation():
    print("Выберите необходимую операцию:")
    op = {"1": "Сложение", "2" :"Вычитание", "3": "Деление", "4": "Умножение"}
    for key in op:
        print(key, '->', op[key])
    op_key = int(input())
    return op_key

def in_complex(str):
    a = input(f"Введите {str} число: ")
    cmplx = a.split('+')
    x = complex(int(cmplx[0]), int(cmplx[1]))
    return x

def in_fraction(str):
    a = input(f"Введите {str} число: ")
    frctn = a.split('/')
    x = Fraction(int(frctn[0]), int(frctn[1]))
    return x

def in_modul():
    print("Выберите тип чисел:")
    type = {"1": "Рациональные числа", "2" :"Комплексные числа"}
    for key in type:
        print(key, '->', type[key])
    type_key = int(input())
    return type_key

def result():
    print(ctrl.result())
