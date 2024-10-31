# 1. Напишите функцию, которая принимает список кортежей от пользователя, где каждый кортеж содержит информацию о студенте (имя, возраст, средний балл).
# Программа должна вывести на экран имена студентов, чей средний балл выше заданного значения.
# Используйте методы кортежей и циклы для обработки данных.Выведите итоговый список на экран с помощью команды print.

def fill_student():
    print('Заполнение данных о студенте. Оставьте пустую строку')
    name = input('Введите имя студента: ')
    if not name:
        return None

    age = int(input('Введите вохраст студента: '))
    score = int(input('Введите средний балл студента: '))

    return name, age, score


def fill_students():
    students = []
    while True:
        student = fill_student()
        if student is None:
            break
        students.append(student)

    return students


def get_passed_students(students, passed_score):
    passed_students = []
    for student in students:
        if student[2] > passed_score:
            passed_students.append(student[0])

    return passed_students


avg_score = int(input('Введите пороговое значение среднего балла: '))  # 90

# [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
print(f'Студенты с средним баллом выше {avg_score} : {get_passed_students(fill_students(), avg_score)}')  # ['Charlie']

# 2. Напишите программу, которая принимает строку от пользователя и разбивает ее на отдельные слова.
# Затем программа должна создать новый кортеж, содержащий длину каждого слова в исходной строке.
# Используйте методы строк и кортежей для обработки данных.

# Программирование это интересно и полезно
print('Длины слов в предложении: ', tuple(len(str_part) for str_part in input('Введите предложение: ').split()))  # (16, 3, 9, 1, 7)
