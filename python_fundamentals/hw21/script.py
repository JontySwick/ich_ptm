# 1. Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте и выводит на экран наиболее часто встречающиеся слова.
# Для решения задачи используйте класс Counter из модуля collections.
# Создайте функцию count_words, которая принимает текст в качестве аргумента и возвращает словарь с количеством вхождений каждого слова.
# Выведите наиболее часто встречающиеся слова и их количество.

from collections import Counter


def count_words(text):
    return Counter([word.lower().strip(',.!?') for word in text.split()])


user_input = input('Введите текст: ')
print(f'Введенный текст: {user_input}')
for word, count in count_words(user_input).most_common():
    print(f'{word}: {count}')

# 2. Напишите программу, которая создает именованный кортеж Person для хранения информации о человеке, включающий поля name, age и city.
# Создайте список объектов Person и выведите информацию о каждом человеке на экран.

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])

for person in [Person('Alice', 25, 'New York'), Person('Bob', 30, 'London'), Person('Carol', 35, 'Paris')]:
    print(f'Name: {person.name}, Age: {person.age}, City: {person.age}')


# 3. Напишите программу, которая принимает словарь от пользователя и ключ,
# и возвращает значение для указанного ключа с использованием метода get или setdefault.
# Создайте функцию get_value_from_dict, которая принимает словарь и ключ в качестве аргументов, и возвращает значение для указанного ключа,
# используя метод get или setdefault в зависимости от выбранного варианта.
# Выведите полученное значение на экран.

def get_value_from_dict(dictionary, key, add_if_empty=True, default_value=0):
    return dictionary.setdefault(key, default_value) if add_if_empty else dictionary.get(key)


my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}

while True:
    user_key = input('Введите ключ для поиска: ')
    is_add_if_empty = input('Использовать метод get (y/n)?') == 'n'

    print(f'Значение для ключа \'{user_key}\': {get_value_from_dict(my_dict, user_key, is_add_if_empty)}')
