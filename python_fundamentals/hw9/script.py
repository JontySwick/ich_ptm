# 1. Напишите программу, которая запрашивает у пользователя строку и определяет, является ли она панграммой.
# Панграмма - это фраза, содержащая все буквы алфавита. Программа должна игнорировать регистр букв и пробелы при проверке панграммы.
# Выведите соответствующее сообщение на экран с помощью команды print. Решить задачу для латиницы.

user_string = input('Введите строку: ')  # The quick brown fox jumps over the lazy dog
a_ord = ord('A')
z_ord = ord('Z')
a_ord_case = ord('a')
z_ord_case = ord('z')
case_shift = a_ord - a_ord_case

is_pangram = True

searching_letter_ord = a_ord
user_string_len = len(user_string)
while searching_letter_ord <= z_ord:
    is_letter_found = False
    start_pos = 0
    while start_pos < user_string_len:
        letter = user_string[start_pos:start_pos+1]
        current_letter_ord = ord(letter)

        # Пропускаем все что не латиница
        if not (a_ord <= current_letter_ord <= z_ord or a_ord_case <= current_letter_ord <= z_ord_case):
            start_pos += 1
            continue

        if current_letter_ord == searching_letter_ord or current_letter_ord + case_shift == searching_letter_ord:
            is_letter_found = True
            break

        start_pos += 1

    if not is_letter_found:
        is_pangram = False
        break

    searching_letter_ord += 1

print('Строка ', '' if is_pangram else 'не ', 'является панграммой.', sep='')

# 2. Напишите программу, которая запрашивает у пользователя строку и выводит на экран количество гласных и согласных букв в ней.
# Используйте функцию len() для подсчета количества букв. Выведите результат на экран с помощью команды print.
# Решить задачу для латиницы.

user_string = input('Введите строку: ')  # Hello World

a_ord = ord('A')
z_ord = ord('Z')
a_ord_case = ord('a')
z_ord_case = ord('z')

vowel_count = 0
consonant_count = 0

start_pos = 0
user_string_len = len(user_string)
while start_pos < user_string_len:
    letter = user_string[start_pos:start_pos+1]
    current_letter_ord = ord(letter)
    start_pos += 1

    # Пропускаем все что не латиница
    if not (a_ord <= current_letter_ord <= z_ord or a_ord_case <= current_letter_ord <= z_ord_case):
        continue

    if letter in 'aeiouyAEIOUY':
        vowel_count += 1
    else:
        consonant_count += 1

print('Количество гласных букв:', vowel_count)
print('Количество согласных букв:', consonant_count)