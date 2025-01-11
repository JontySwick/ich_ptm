# 1. Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов только четных чисел из списка,
# используя функциональные подходы (например, map, filter и reduce).


def get_sum_sqr_of_odd_numbers(numbers: list[int]) -> int:
    return sum(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))


# 4, 6, 3, 4, 2, 3, 9, 0, 7
print(f'Результат: {get_sum_sqr_of_odd_numbers([int(number) for number in input("Введите числа: ").split(", ")])}')


# 2. Напишите функцию, которая принимает на вход список функций и значение,
# а затем применяет композицию этих функций к значению, возвращая конечный результат.

def compose_functions(funcs, initial_value):
    for func in funcs:
        initial_value = func(initial_value)

    return initial_value


add_one = lambda x: x + 1
double = lambda x: x * 2
subtract_three = lambda x: x - 3

functions = [add_one, double, subtract_three, print]

compose_functions(functions, 5)
