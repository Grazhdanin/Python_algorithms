"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


import random
import time

my_list = []
my_dict = {}


def timer(func):
    def tmp(*args):
        start_val = time.time()
        res = func(*args)
        print(f'Время выполнения функции: {time.time()-start_val}')
    return tmp


@timer
def rand_list(val):
    print(f'Выполняется запонение "list"...')
    for i in range(val):
       my_list.append(i)


@timer
def rand_dict(val):
    print(f'Выполняется запонение "dict"...')
    for i in range(val):
        my_dict[i] = i
    #my_dict.update({a: a for a in range(val)})


@timer
def get_from_dict(val, number):
    print(f'Выполняется поиск числа "{number}" в "dicе"')
    if val.get(number) is not None:
        print('Найдено')


@timer
def get_from_list(val, number):
    print(f'Выполняется поиск числа "{number}" в "list"')
    for el in val:
        if el == number:
            print('Найдено')


rand_dict(1000000)
rand_list(1000000)
get_from_dict(my_dict, 100000)
get_from_list(my_list, 100000)
