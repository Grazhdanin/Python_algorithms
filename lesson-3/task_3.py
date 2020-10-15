"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

import hashlib

def number_substrings(line):

    unique = set()
    start = len(line)

    for el in range(start):
        if el == 0:
            start = len(line) - 1
        else:
            start = len(line)
        for r_el in range(start, el, -1):
            unique.add(hashlib.sha256(line[el:r_el].encode()).hexdigest())

    print(f'В строке "{line}" количество подстрок: {len(unique)}')

number_substrings('papa')