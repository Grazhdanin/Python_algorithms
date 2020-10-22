"""
Задание 2.
Предложить еще какие-гибудь варианты (механизмы, библиотеки) оптимизации и
доказать (наглядно, кодом) их эффективность
"""

"""
Давайте разделим изначальный код примера на два файла с названиями test_cython.py и test_module.pyx:

# название файла: test_module.pyx

def sum_of_lists(ls):
    '''считает сумму значений переданного списка списков'''

    s = 0
    for l in ls:
        for val in l:
            s += val

    return s
Наш главный файл должен импортировать эту функцию с файла test_module.pyx:

# название файла: test_cython.py

from test_module import *

# создать список списков целых чисел
smallrange = list(range(10000))
inlist = [smallrange, smallrange, smallrange, smallrange]

# получить сумму
list_sum = sum_of_lists(inlist)

print(list_sum)
Теперь напишем скрипт setup.py для компиляции нашего модуля при помощи Cython:

# название файла: setup.py

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("test_module.pyx")
)

В этом случае Cython должен улучшил производительность нашей программы почти вдвое по сравнению с первым вариантом.
"""

