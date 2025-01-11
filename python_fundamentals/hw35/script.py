import requests

# 1. Напишите функцию get_response(url), которая отправляет GET-запрос по заданному URL-адресу и возвращает объект ответа.
# Затем выведите следующую информацию об ответе:
# - Код состояния (status code)
# - Текст ответа (response text)
# - Заголовки ответа (response headers)

# def get_response(uri):
#     return requests.get(uri)
#
#
# response = get_response(input('Enter url: '))
#
# print("Status Code:", response.status_code)
# print("Response Text:", response.text)
# print("Response Headers:", response.headers)

# 2. Напишите функцию find_common_words(url_list), которая принимает список URL-адресов и возвращает список наиболее часто встречающихся слов на веб-страницах.
# Для каждого URL-адреса функция должна получить содержимое страницы с помощью запроса GET и использовать регулярные выражения для извлечения слов.
# Затем функция должна подсчитать количество вхождений каждого слова и вернуть наиболее часто встречающиеся слова в порядке убывания частоты.

from bs4 import BeautifulSoup
import re
from collections import Counter
def find_common_words(url_list):
    count = Counter()
    for url in url_list:
        response = requests.get(url)
        words = BeautifulSoup (response.text, 'html.parser')
        words = re.findall(r'\b[a-z]+\b', words.text, re.I)
        count.update(map(str.lower, words))
    return count

urls = [
    'https://google.com',
    'https://stepik.org',
    'https://github.com',
    'https://www.bahn.de'
]

print(find_common_words(urls).most_common(10))