import os
import dotenv
from pathlib import Path
import mysql.connector

dotenv.load_dotenv(Path('../.env'))
databases_name = 'ich_edit'

dbconfig = {
    'host': os.environ.get('DB_READ_HOST'),
    'user': os.environ.get('DB_READ_USER'),
    'password': os.environ.get('DB_READ_PASSWORD'),
    'database': databases_name
}

# 1. В базе данных ich_edit три таблицы.
# Users с полями (id, name, age),
# Products с полями (pid, prod, quantity)
# и Sales с полями (sid, id, pid).
# Программа должна запросить у пользователя название таблицы и вывести все ее строки или сообщение, что такой таблицы нет.

connection = mysql.connector.connect(**dbconfig)
cursor = connection.cursor()

cursor.execute('SHOW TABLES')
tables = dict(enumerate(map(lambda x: x[0], cursor.fetchall()), 1))

print('Tables list:')
for index, table in tables.items():
    print(f'{index}. {table}')

table_number = int(input('Enter only number of table: '))

if table_name := tables.get(table_number):
    cursor.execute(f'DESCRIBE {databases_name}.{tables[table_number]}')
    print(tuple(map(lambda x: x[0], cursor.fetchall())))

    cursor.execute(f'SELECT * FROM {databases_name}.{tables[table_number]}')
    rows = cursor.fetchall()
    print(*rows, sep='\n')
else:
    print('Not exist table selected')

connection.close()

# 2. В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).
# Программа должна вывести все имена из таблицы users, дать пользователю выбрать одно из них и вывести все покупки этого пользователя.

connection = mysql.connector.connect(**dbconfig)
cursor = connection.cursor()
cursor.execute(f'SELECT id, name FROM {databases_name}.users')

print('Select user to show sales:')
users = {k: v for k, v in cursor.fetchall()}
for k, v in users.items():
    print(f'{k}. {v}')

selected_user = None
uid = 0

while selected_user is None:
    uid = int(input('Enter user number: '))
    selected_user = users.get(uid)

cursor.execute(
    '''
    SELECT p.*
    FROM ich_edit.users u 
    LEFT JOIN ich_edit.sales s ON s.id = u.id AND u.id = %(uid)s
    LEFT JOIN ich_edit.product p ON p.pid = s.pid
    WHERE u.id = %(uid)s
    ''',
    {'uid': uid})

result = cursor.fetchall()
print(*result, sep='\n')

cursor.close()
connection.close()
