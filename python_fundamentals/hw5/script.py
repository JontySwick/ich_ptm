# 1. Напишите программу, которая запрашивает у пользователя три числа и выводит их в порядке возрастания, разделенные
# запятой. Используйте условные операторы и вложенные условия для решения задачи.
# Предполагается, что все три числа различны.

a = int(input('Enter 1st number: '))
b = int(input('Enter 2st number: '))
c = int(input('Enter 3ed number: '))

min_number = a
max_number = a
middle_number = a

if min_number > b:
    min_number = b
if min_number > c:
    min_number = c

if max_number < b:
    max_number = b
if max_number < c:
    max_number = c

if min_number < b < max_number:
    middle_number = b
if min_number < c < max_number:
    middle_number = c

print(min_number, middle_number, max_number, sep=', ')

# 2. Напишите программу, которая запрашивает у пользователя год и проверяет, является ли он високосным.
# Год является високосным, если он делится на 4 без остатка, но не делится на 100 без остатка, за исключением годов,
# которые делятся на 400 без остатка. Выведите соответствующее сообщение на экран с помощью команды print.
year = int(input('Enter year: '))
is_leap_year = year % 4 == 0 and (year % 400 == 0 or not year % 100 == 0)
print('It is', 'a' if is_leap_year else 'not a', 'leap year')