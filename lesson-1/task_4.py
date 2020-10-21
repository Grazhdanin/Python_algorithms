"""
Задание 4.

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
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

def authorization_for(users, user_name, user_password):  # O(n)
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return "Доступ разрешен"
            elif value['password'] == user_password and not value['activation']:
                return "Учетная запись не активна! Активируйтесь!"
            elif value['password'] != user_password:
                return "Не верный пароль"

    return "Данного пользователя не существует"


def authorization_get(users, user_name, user_password):  # O(1)
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activation']:
            return "Доступ разрешен"
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:
            return "Учетная запись не активна! Активируйтесь!"
        elif users[user_name]['password'] != user_password:
            return "Пароль не верный"
    else:
        return "Пользователя не существует"


my_users = {'user1': {'password': '12345', 'activation': True},
            'user2': {'password': '54321', 'activation': False},
            'user3': {'password': '89320', 'activation': True}
            }

print(authorization_for(my_users, 'user1', '12345'))
print(authorization_get(my_users, 'user1', '12345'))

print(authorization_for(my_users, 'user2', '54321'))
print(authorization_get(my_users, 'user2', '54321'))

print(authorization_for(my_users, 'user4', '11111'))
print(authorization_get(my_users, 'user4', '11111'))