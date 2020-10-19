"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit


def filling_dict(val):
    a = dict()
    for i in range(val):
        a[str(i)] = i


def filling_o_dict(val):
    a = OrderedDict()
    for i in range(val):
        a[str(i)] = i


def for_every_kv_dict(val):
    for key, value in val.items():
        a = key
        b = value


def for_every_kv_o_dict(val):
    for key, value in val.items():
        a = key
        b = value


def list_sorting_dict(val):
    a = sorted(val.items(), key=lambda item: item[1])


def list_sorting_o_dict(val):
    a = sorted(val.items(), key=lambda item: item[1])


def popitem_dict(val):
    for i in range(len(val)):
        a = val.popitem()


def popitem_o_dict(val):
    for i in range(len(val)):
        a = val.popitem()


val_1 = 1000
my_dict = {str(i): i for i in range(1000)}
o_my_dict = OrderedDict(my_dict)

print(timeit("filling_dict(val_1)", setup="from __main__ import filling_dict, val_1", number=1000))
print(timeit("filling_o_dict(val_1)", setup="from __main__ import filling_o_dict, val_1", number=1000))
print(timeit("for_every_kv_dict(my_dict)", setup="from __main__ import for_every_kv_dict, my_dict", number=1000))
print(timeit("for_every_kv_o_dict(o_my_dict)", setup="from __main__ import for_every_kv_o_dict, o_my_dict", number=1000))
print(timeit("list_sorting_dict(my_dict)", setup="from __main__ import list_sorting_dict, my_dict", number=1000))
print(timeit("list_sorting_o_dict(o_my_dict)", setup="from __main__ import list_sorting_o_dict, o_my_dict", number=1000))
print(timeit("popitem_dict(my_dict)", setup="from __main__ import popitem_dict, my_dict", number=1000))
print(timeit("popitem_o_dict(o_my_dict)", setup="from __main__ import popitem_o_dict, o_my_dict", number=1000))

#OrderedDict уступает в скорости dict

"""                                       
0.3642026                                    
0.45028850000000004
0.03608729999999993
0.08098810000000001
0.14876359999999988
0.18783869999999991
0.00034890000000009636
0.0004320999999998243
"""

"""
0.3499622
0.4379292
0.039310899999999926
0.07731929999999998
0.1289610000000001
0.16626549999999995
0.0003375000000001016
0.00041530000000000733
"""

"""
0.4826797
0.49556770000000006
0.0408636
0.0829892000000001
0.13479449999999993
0.19115680000000013
0.0003404999999998548
0.00041290000000016036
"""
