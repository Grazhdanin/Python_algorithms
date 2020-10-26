"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

from statistics import median
from random import randint


def median_with_sort(array, middle):
    return sorted(array)[middle]


def median_no_sort(array):
    """ Вычисление медианы списка без сортировки """
    for i in range(len(array)):
        result = 0
        temp = 0
        for j in range(len(array)): 
            if j != i:
                if array[j] > array[i]:
                    result += 1
                elif array[j] < array[i]:
                    result -= 1
                else:
                    temp += 1


        if result == 0 or result == temp:
            return array[i]
        elif temp >= abs(result) and result < temp:
            if result > 0 and (temp - result) % 2 == 0:
                return array[i]
            elif result < 0 and (temp + result) % 2 == 0:
                return array[i]



m = randint(0, 15)
array = [2 * randint(1, 10) + 1 for x in range(2 * m + 1)]
print(f'{array}\nМедиана: {median(array)} (median), {median_no_sort(array)} (поиск), \
{median_with_sort(array, m)} (сортировка)\n')

