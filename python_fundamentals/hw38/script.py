# 1. Доработать мини-интерфейс к базе данных, который был сделан на занятии. Новые возможности интерфейса:
# Ввести список полей выбранной таблицы.
# При вводе искомого значения добавить возможность выбора знака - найти записи, в которых выбранное поле больше, меньше или равно введенному значению.

import os
import dotenv
from pathlib import Path
import mysql.connector


dotenv.load_dotenv(Path('../.env'))
databases_name = 'world'

dbconfig = {
    'host': os.environ.get('DB_READ_HOST'),
    'user': os.environ.get('DB_READ_USER'),
    'password': os.environ.get('DB_READ_PASSWORD'),
    'database': databases_name
}
connection = mysql.connector.connect(**dbconfig)
cursor = connection.cursor()


def get_table_columns(name_table):
    non_display = ('Code', 'Code2', 'ID', 'CountryCode')
    cursor.execute(f'DESCRIBE {name_table}')
    return [i for i, *_ in cursor.fetchall() if i not in non_display]

def choise_colums(colums:list):
    print("Отлично! Вот список доступных колонок, которые я могу отобразить:")
    dict_colums = dict(enumerate(colums, 1))
    for key, value in dict_colums.items():
        print(f'\t{key}: {value}')
    num_kol = input('Укажите номера колонок, через через пробел, которые необходимо отобразить: ').split()
    return [dict_colums[int(i)] for i in num_kol]

def make_select(colums):
    return "SELECT " + ', '.join(colums) + " FROM "

def get_all_name(table_name):
    cursor.execute('select Name from ' + table_name)
    return map(lambda x: x[0], cursor.fetchall())

# Доработать форматирование
def show_bese_info():
    tab = 'country'
    colums = choise_colums(get_table_columns(tab))
    select = make_select(colums) + tab
    cursor.execute(select)
    print(*cursor.fetchall(), sep='\n')

def show_country_info():
    print("Отлично! Вот список доступных стран, города которых, я могу отобразить:")
    dict_colums = dict(enumerate(get_all_name('country'), 1))
    for key, value in dict_colums.items():
        print(f'\t{key}: {value}')
    num = input('Укажите номер страны, города которой необходимо отобразить: ')
    country_n = dict_colums[int(num)]
    colums = choise_colums(get_table_columns('city'))

    select = (f'{make_select(colums)} city '
              f'where CountryCode = (select Code from country where `Name` = "{country_n}")')
    cursor.execute(select)
    print(*cursor.fetchall(), sep='\n')

def show_city_info():
    print("Отлично! Вот список доступных городов, которые я могу отобразить:")
    dict_colums = dict(enumerate(get_all_name('city'), 1))
    for key, value in dict_colums.items():
        print(f'\t{key}: {value}')
    nums = input('Укажите номера городов которые необходимо отобразить: ').split()
    colums = choise_colums(get_table_columns('city'))
    citys = ', '.join(f'"{dict_colums[int(i)]}"' for i in nums)
    select = (f'{make_select(colums)} city '
              f'where Name in ({citys})')
    cursor.execute(select)
    print(*cursor.fetchall(), sep='\n')

print('Добрый день! Я сервис, предоставляющий информацию по странам и городам!\n'
      'Я могу показать Вам общую информацию по:\n'
      ' 1 - базовую информацию по всем странам или городам\n'
      ' 2 - информацию по какой либо конкретной стране\n'
      ' 3 - информацию по какому-то либо городу')

all_power = {
    1: show_bese_info,
    2: show_country_info,
    3: show_city_info
}
choice = int(input('Сделайте свой выбор: '))

all_power[choice]()