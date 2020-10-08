"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import sys
import random

number = random.randint(1, 100)
print(f'n = {number}')

sys.setrecursionlimit(10000)


def operation(n, sum_n=0, rav_n=1):
    if sum_n == rav_n:
        return print('Равенство доказано')
    elif sum_n < rav_n:
        rav_n = n * (n + 1) / 2
        operation(n, sum_n+1, rav_n)

operation(number)