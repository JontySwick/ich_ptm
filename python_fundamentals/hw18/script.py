# Написать программу, вычисляющую факториал числа.
# Решить задачу с помощью рекурсии.
def get_factorial(n):
    if n == 0:
        return 1

    return n * get_factorial(n - 1)


user_number = int(input('Введите число: '))

print(f'Факториал числа {user_number} = {get_factorial(user_number)}')


# Напишите программу, которая использует рекурсию для вычисления суммы цифр числа.
# Создайте функцию sum_digits, которая принимает один аргумент - число, для которого нужно вычислить сумму цифр.
# Используйте условие выхода из рекурсии, когда число состоит из одной цифры. Выведите результат на экран.
def sum_digits(number):
    if abs(number) < 10:
        return number

    return sum_digits(number // 10) + number % 10


user_number = input('Введите число: ')  # 12345

print(f'Сумма цифр числа {user_number} равна {sum_digits(int(user_number))}')
