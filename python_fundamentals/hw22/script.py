# 1. Напишите программу, которая открывает файл, считывает из него два числа и выполняет операцию их деления.
# Если число отрицательное, выбросите исключение ValueError с сообщением "Число должно быть положительным".
# Обработайте исключение и выведите соответствующее сообщение.

from time import sleep

with open('file_with_negative_numbers.txt', 'r', encoding='utf-8') as f:
    for line in f:
        try:
            a, b = [float(i) for i in line.strip().split(' ')]
            if a < 0 or b < 0:
                raise ValueError
            print(f'{a} / {b} = {a / b}')
        except ValueError:
            print('Число должно быть положительным')

# 2. Напишите программу, которая открывает файл, считывает его содержимое и выполняет операции над числами в файле.
# Обработайте возможные исключения при открытии файла (FileNotFoundError) и при выполнении операций над числами (ValueError, ZeroDivisionError).
# Используйте конструкцию try-except-finally для обработки исключений и закрытия файла в блоке finally.

file = None
try:
    #file = open('not_exists_file.txt', 'r', encoding='utf-8')
    file = open('file_with_too_many_errors.txt', 'r', encoding='utf-8')
    for line in file:
        try:
            a, b = [int(i) for i in line.strip().split(' ')]
            if a < 0 or b < 0:
                raise ValueError
            print(a / b)
        except ValueError:
            print('Одно из чисел отрицательное. Строка пропущена')
        except ZeroDivisionError:
            print('На ноль делить нельзя. Строка пропущена')
except FileNotFoundError:
    print('Файл не найден')
finally:
    if file:
        file.close()