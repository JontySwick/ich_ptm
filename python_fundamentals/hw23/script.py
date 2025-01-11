# 1. Напишите программу, которая генерирует и выводит квадраты чисел от 1 до N с использованием генераторного выражения.
# Реализуйте функцию generate_squares, которая принимает число N в качестве аргумента и использует генераторное выражение для генерации квадратов чисел.
# Затем выведите квадраты чисел на экран.

def generate_squares(n):
    if not isinstance(n, int) or n < 2:
        raise ValueError('n must be greater than 1 and integer type')
    yield from (i ** 2 for i in range(1, n + 1))        


for square in enumerate(generate_squares(5)):
    print(square)


# 2. Напишите генератор, который будет генерировать бесконечную последовательность Фибоначчи.
# Каждый раз, когда генератор вызывается, он должен возвращать следующее число последовательности.
# Напишите программу, которая будет использовать этот генератор для вывода первых N чисел Фибоначчи.

def fibonacci_generator():
    f1, f2 = 0, 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2


fibonacci = fibonacci_generator()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
