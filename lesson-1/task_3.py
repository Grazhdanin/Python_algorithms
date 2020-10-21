"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

company = {'company_1': 113000,
           'company_2': 99000,
           'company_3': 109000,
           'company_4': 111000,
           'company_5': 111000,
           'company_6': 123000,
           'company_7': 13000,
           'company_8': 11000}

# O(n)

def max_company(company):
    max_num = {}
    b_d = dict(company)
    for el in range(3):
        maximum =max(b_d.items(), key=lambda q: q[1])
        del b_d[maximum[0]]
        max_num[maximum[0]] = maximum[1]
    return max_num

print(max_company(company))

#################################################################



def top_profit(company):
    max_profit = 0
    max_profit_company = {}
    for key, value in comp_prof.items():
        if value > max_profit:
            max_profit = value
            max_profit_company = {}
            max_profit_company.setdefault(key, value)
    return max_profit_company



def top_3(company):
    top_3_comp = []
    for el in range(3):
        comp = top_profit(company)
        top_3_comp.extend(*comp.items())
        company.pop(*comp)
    return top_3_comp


print(top_3(company))

######################################################################

# O(n log n)

def top_companies(company):
    top_company = list(company.items())
    top_company.sort(key=lambda x: x[-1])
    top_company.reverse()
    for i in top_company[:3]:
        print(f'Прибыль компании {i[0]} составляет {i[1]}')


top_companies(company)

"""
Таким образом, первое решение является более оптимальным, поскольку,
оно задействует меньшее количество шагов, согласно О-нотации, является более простым
"""
