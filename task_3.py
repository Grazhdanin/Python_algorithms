"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""


from collections import deque
import timeit
import cProfile

def list_append(value):
    my_list = []
    for el in range(value):
        my_list.append(el)
    return my_list

# print(list_append(100))


def deque_append(value):
    my_list = deque()
    for el in range(value):
        my_list.append(el)
    return my_list

# print(deque_append(100))

x = list_append(100)
y = deque_append(100)
x_1 = list(range(100, 20, -1))
y_1 = deque(range(100, 20, -1))


def list_append_left(value):
    my_list = x
    for el in range(value):
        my_list.insert(0, el)
    return my_list

# print(list_append_left(100))


def deque_append_left(value):
    my_list = deque(y)
    for el in range(value):
        my_list.appendleft(el)
    return my_list

# print(deque_append_left(100))


def list_extend(list_range):
    my_list = x
    my_list.extend(list_range)
    return my_list

# print(list_extend(x_1))


def deque_extend(list_range):
    my_list = deque(y)
    my_list.extend(list_range)
    return my_list

# print(deque_extend(x_1))


def list_extend_left(list_range):
    my_list = x
    for el in list_range:
        my_list.insert(0, el)
    return my_list

# print(list_extend_left(x_1))


def deque_extend_left(list_range):
    my_list = y
    my_list.extendleft(list_range)
    return my_list

# print(deque_extend_left(y_1))


def list_pop(list_range):
    for el in range(len(list_range) - 1):
        list_range.pop()
    return list_range

# print(list_pop(x))


def deque_pop(list_range):
    for el in range(len(list_range) - 1):
        list_range.pop()
    return list_range

# print(deque_pop(y))

def list_pop_left(list_range):
    for el in range(len(list_range) - 1):
        list_range.pop(0)
    return list_range

# print(list_pop_left(x_1))

def deque_pop_left(list_range):
    for el in range(len(list_range) - 1):
        list_range.popleft()
    return list_range

# print(deque_pop_left(y_1))



value = 100
list_range = range(100, 20, -1)

print(timeit.timeit("list_append(value)", setup="from __main__ import list_append, value", number=1000))
print(timeit.timeit("deque_append(value)", setup="from __main__ import deque_append, value", number=1000))
print(timeit.timeit("list_append_left(value)", setup="from __main__ import list_append_left, value", number=1000))
print(timeit.timeit("deque_append_left(value)", setup="from __main__ import deque_append_left, value", number=1000))
print(timeit.timeit("list_extend(list_range)", setup="from __main__ import list_extend, list_range", number=1000))
print(timeit.timeit("deque_extend(list_range)", setup="from __main__ import deque_extend, list_range", number=1000))
print(timeit.timeit("list_extend_left(list_range)", setup="from __main__ import list_extend_left, list_range", number=1000))
print(timeit.timeit("deque_extend_left(list_range)", setup="from __main__ import deque_extend_left, list_range", number=1000))
print(timeit.timeit("list_pop(x_1)", setup="from __main__ import list_pop, x_1", number=1000))
print(timeit.timeit("deque_pop(y_1)", setup="from __main__ import deque_pop, y_1", number=1000))
print(timeit.timeit("list_pop_left(x_1)", setup="from __main__ import list_pop_left, x_1", number=1000))
print(timeit.timeit("deque_pop_left(y_1)", setup="from __main__ import deque_pop_left, y_1", number=1000))




"""
 список (list) немного уступает по добавлению и удалениею элеметов в конце очереди, 
 но значительно проигрывает в скорсти по дабовлению и удалению элементов в начале очереди  очередь (deque)
"""
