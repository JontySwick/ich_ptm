# 1. Напишите декоратор validate_args, который будет проверять типы аргументов функции и выводить сообщение об ошибке,
# если переданы аргументы неправильного типа.
# Декоратор должен принимать ожидаемые типы аргументов в качестве параметров.

def validate_args(*args, **kwargs):
    init_args = args
    init_kwargs = kwargs

    def decorator(func):
        def validator(*args, **kwargs):
            for value, expected_type in zip(args, init_args):
                if type(value) is not expected_type:
                    raise TypeError(f'Position argument {value} has type {type(value)}. Expected type: {type}')
            for i, j in zip(sorted(kwargs.items()), sorted(init_kwargs.items())):
                if type(i[1]) is not j[1]:
                    raise TypeError(f'Named argument <{i[0]}> has wrong type: {type(i[1])}. The right type: {j[1]}')

            return func(*args, **kwargs)

        return validator

    return decorator


@validate_args(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")


greet(25, "Анна")  # Все аргументы имеют правильные типы
greet("25", "Анна")  # Возникнет исключение TypeError

# 2. Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов функции в лог-файл.
# Каждый вызов функции должен быть записан на новой строке в формате "Аргументы: <аргументы>, Результат: <результат>".
# Используйте модуль logging для записи в лог-файл.
import functools
import logging


def log_args(func):
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(message)s', filename='./args.log', level=logging.INFO)

    @functools.wraps(func)
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Аргументы: {args}, {kwargs}, Результат: {result}')
        return result

    return decorator


@log_args
def add(a, b):
    return a + b


add(2, 3)
add(5, 7)
