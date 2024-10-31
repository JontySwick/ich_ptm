# 1. Напишите программу, которая запрашивает у пользователя его имя, возраст и место проживания, а затем выводит их в
# следующем формате: "Привет, меня зовут {0}. Мне {1} лет. Я живу в {2}." Вместо {0}, {1} и {2} подставьте
# соответствующие значения. Используйте метод format() для форматирования строки. Потом попробуйте использовать
# f-строку. Выведите результат на экран с помощью команды print.

print(
    'Привет, меня зовут {0}. Мне {1} лет. Я живу в {2}.'
    .format(
        input('Введите ваше имя: '),
        input('Введите ваш возраст: '),
        input('Введите ваше место проживания: ')
    )
)

# 2. Напишите программу, которая запрашивает у пользователя два числа и выводит их сумму и произведение в следующем
# формате: "Сумма: {sum:.2f}, Произведение: {product:.2f}" Вместо {sum:.2f} и {product:.2f} подставьте
# соответствующие значения, округленные до двух десятичных знаков. Используйте f-строки с использованием форматных
# спецификаторов для форматирования чисел. Выведите результат на экран с помощью команды print.

d1 = float(input('Введите первое число: ')) # 3.14159
d2 = float(input('Введите второе число: ')) # 2.71828

summ = d1 + d2
product = d1 * d2

print(f'Сумма: {summ:.2f}, Произведение: {product:.2f}')
