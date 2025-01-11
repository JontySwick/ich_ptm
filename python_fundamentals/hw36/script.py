# 1. Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы,
# использует библиотеку Beautiful Soup для парсинга HTML и выводит список всех ссылок на странице.

from bs4 import BeautifulSoup
import requests

[print(tag.attrs.get('href')) for tag in BeautifulSoup(requests.get(input('Enter page url: ')).text, 'html.parser').find_all('a')]


# 2. Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и уровень заголовков,
# а затем использует библиотеку Beautiful Soup для парсинга HTML и извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом.

[print(tag.get_text()) for tag in BeautifulSoup(requests.get(input('Enter page url: ')).text, 'html.parser').find_all('h'+str(int(input('Enter header size: '))))]