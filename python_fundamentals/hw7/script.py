# 1. Напишите программу, которая запрашивает у пользователя натуральное десятичное число и выводит его двоичное представление.
# Реализуйте алгоритм перевода числа в двоичную систему счисления, используя основные концепции представления чисел.
# Выведите полученное представление числа на экран.

dividend = int(input('Введите натуральное десятичное число: '))

binary = ''
while dividend > 1:
    binary = str(dividend % 2) + binary
    dividend = dividend // 2

binary = str(dividend) + binary

print('Двоичное представление числа:', binary)

# 2. Напишите программу, принимающую число с плавающей точкой и округляющую его до целого числа в соответствии с правилами школьной математики.
# Использовать модуль math и методы из него нельзя.
# Учесть, что программа должна корректно работать с отрицательными числами.

n = float(input('Введите вещественное число: '))
reminded = n % 1
multiplier = 1 if n >= 0 else -1
n = abs(n)
if reminded >= 0.5:
    n += 1-reminded
else:
    n -= reminded

print('Округленное значение:', n*multiplier)