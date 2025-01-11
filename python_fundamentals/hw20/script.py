# 1. Напишите функцию merge_dicts, которая принимает произвольное количество словарей в качестве аргументов
# и возвращает новый словарь, объединяющий все входные словари.
# Если ключи повторяются, значения должны быть объединены в список.
# Функция должна использовать аргумент *args для принятия произвольного числа аргументов словаря.

def merge_dicts(*dicts):
    merged_dict = {}

    for dictionary in dicts:
        for key, value in dictionary.items():
            merged_dict.setdefault(key, []).append(value)

    return merged_dict


print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}))


# 2. Напишите программу, которая принимает строку от пользователя и подсчитывает количество уникальных символов в этой строке.
# Создайте функцию count_unique_chars, которая принимает строку и возвращает количество уникальных символов.
# Выведите результат на экран.

def count_unique_chars(string):
    char_dict = {}
    [char_dict.setdefault(char, []).append(char) for char in string]

    return len(char_dict)


print(count_unique_chars('hello'))


# 3. Напишите программу, которая создает словарь, содержащий информацию о студентах и их оценках.
# Ключами словаря являются имена студентов, а значениями - списки оценок.
# Создайте функцию calculate_average_grade, которая принимает словарь с оценками студентов и вычисляет средний балл для каждого студента.
# Функция должна возвращать новый словарь, в котором ключами являются имена студентов, а значениями - их средний балл.
# Выведите результат на экран.


def fill_students():
    students = {}
    students_count = int(input('Введите количество студентов: '))
    while students_count:
        students.setdefault(input('Bведите имя студента: '),
                            [float(n) for n in input('Введите оценки через пробел: ').split()])
        students_count -= 1
    return students


def calculate_average_grade(students):
    return {name: sum(grades) / len(grades) for name, grades in students.items()}


# Alice
# 85 90 92
# Bob
# 78 80 84
# Carol
# 92 88 95
print(calculate_average_grade(fill_students()))
