# 1. Напишите программу, которая запрашивает у пользователя целое число и определяет, является ли оно палиндромом.
# Число является палиндромом, если оно читается одинаково слева направо и справа налево.
# Выведите соответствующее сообщение на экран с помощью команды print.
# Используйте математические операции. Работу со строками использовать нельзя.

d = int(input('Введите целое число: '))
original_d = d
reversed_d = 0
multiplier = 10
while d > 0:
    number = d % multiplier
    d //= multiplier
    reversed_d = reversed_d * multiplier + number

print('Число', original_d if original_d == reversed_d else 'не', 'является палиндромом.')



# 2. Напишите программу, которая запрашивает у пользователя целое число и проверяет, является ли оно числом Армстронга.
# Число Армстронга - это число, которое равно сумме своих цифр, возведенных в степень, равную количеству цифр в числе.
# Выведите соответствующее сообщение на экран с помощью команды print.

d = int(input('Введите целое число: '))
if d < 1:
    print('К вводу допускаются только числа больше 0')

length = 0
while d // 10**length:
    length += 1

original_d = d
multiplier = 10
summ = 0
while d > 0:
    number = d % multiplier
    d //= multiplier
    summ += number ** length

print('Число', original_d if original_d == summ else 'не', 'является числом Армстронга.')