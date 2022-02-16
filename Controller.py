from operator import mod
import view
import fract_md as fract
import complex_md as cmplx

def get_operation():
    global op
    op = view.in_operation()
        

def get_modul():
    global md
    md = view.in_modul()

def start():
    get_modul() # Получение типа обрабатываемых чисел: рациональные или комплексные
    get_operation() # Получение типа операции: сложение\вычитание\деление\умножение
    if md==1: result = fract.input(op)
    elif md==2: result = cmplx.input(op)
    view.print_res(result)