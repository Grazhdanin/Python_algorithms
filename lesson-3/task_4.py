"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib
from uuid import uuid4

url_cach = dict()
salt = uuid4().hex

def cach_web_page(url):

    if url_cach.get(url):
        print(f'Данный url: {url} присутствует в кэше')
    else:
        res = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        url_cach[url] = res
        print(url_cach)


cach_web_page('https://yandex.ru')
cach_web_page('https://yandex.ru')

