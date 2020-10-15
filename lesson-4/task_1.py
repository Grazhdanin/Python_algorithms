"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit
import random

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [num for num in range(len(nums)) if nums[num] % 2 == 0]
    return new_arr


user_array = [random.randint(0, 100) for num in range(0, 100)]

my_list = [2, 4, 5, 6]
print(func_2(my_list))
print(func_1(my_list))

print(
    f'{timeit(f"func_1({user_array})", setup="from __main__ import func_1", number=1000)}')
print(f'{timeit(f"func_2({user_array})", setup="from __main__ import func_2", number=1000)}')

"""Заменил цикл, на генераторное выражения, хотя они оба имеют линейную сложность, 
генераторное выражение использует меньше памяти, возможно из-за этого его время выполнения меньше"""

