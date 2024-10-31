# 1. Напишите программу, которая запрашивает у пользователя строку и преобразует ее, удаляя все гласные буквы из строки.
# Используйте метод replace() для замены гласных букв на пустую строку.
# Выведите преобразованную строку на экран с помощью команды print.

print('Результат:',
      input('Введите строку: ').replace('aeiouyAEIOUY', '')
      .replace('a', '')
      .replace('e', '')
      .replace('i', '')
      .replace('o', '')
      .replace('u', '')
      .replace('y', '')
      .replace('A', '')
      .replace('E', '')
      .replace('I', '')
      .replace('O', '')
      .replace('U', '')
      .replace('Y', '')
      )

# 2. Напишите программу, которая запрашивает у пользователя строку и определяет, содержит ли она только уникальные символы.
# Если все символы в строке уникальны, выведите соответствующее сообщение на экран.
# В противном случае выведите сообщение о том, какие символы повторяются.
# Не используйте множества и подобные структуры данных, которые мы пока не изучали, для проверки уникальности символов.

user_string = input('Введите строку: ')  # Python
start_pos = 0
user_string_len = len(user_string)
repeated_symbols = ''
while start_pos < user_string_len:
    letter = user_string[start_pos]
    start_pos += 1

    if user_string.count(letter) > 1:
        if repeated_symbols:
            repeated_symbols += ' и '
        repeated_symbols += f'`{letter}`'

if repeated_symbols:
    print(f'Символы {repeated_symbols} повторяются.')
else:
    print('Все символы в строке уникальны.')

# 3. Напишите программу, которая запрашивает у пользователя строку и выравнивает ее по центру с заданной шириной.
# Если строка не может быть выровнена по центру из-за нечетной ширины, она должна быть выровнена смещением вправо.
# Используйте методы center() и rjust() для выравнивания строки.

user_string = input('Введите строку: ')  # Python
width = int(input('Введите ширину: '))  # 10

if (width - len(user_string)) % 2:
    print(user_string.rjust(width))
else:
    print(user_string.center(width))
