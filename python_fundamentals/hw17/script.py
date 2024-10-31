# 1. Напишите программу, которая принимает список чисел от пользователя и передает его в функцию modify_list,
# которая изменяет элементы списка. Функция должна умножить нечетные числа на 2, а четные числа разделить на 2.
# Выведите измененный список на экран.
# Объясните, почему изменения происходят только внутри функции и как работают изменяемые и неизменяемые параметры.
def modify_list(numbers):
    new_numbers = []
    for number in numbers:
        number = float(number)
        new_numbers.append(number * 2 if number % 2 else number / 2)

    return new_numbers


user_numbers = input('Введите список чисел, разделенных пробелами: ').split()  # 1 2 3 4 5

print('Измененный список чисел:', modify_list(user_numbers))  # [2, 1, 6, 2, 10]


# 2. Напишите программу, которая принимает произвольное количество аргументов от пользователя и передает их в функцию calculate_sum,
# которая возвращает сумму всех аргументов. Используйте оператор * при передаче аргументов в функцию.
# Выведите результат на экран.
def calculate_sum(*numbers):
    return sum(numbers)


user_numbers = [int(number) for number in input('Введите числа, разделенные пробелами: ').split()]  # 1 2 3 4 5

print('Сумма чисел:', calculate_sum(*user_numbers))  # 15
