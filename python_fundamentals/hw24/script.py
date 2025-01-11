# 1. Напишите генератор, который будет принимать на вход числа и возвращать их сумму.
# Генератор должен использовать инструкцию yield для возврата текущей суммы и должен продолжать принимать новые числа для добавления к сумме.
# Если генератор получает на вход число 0, он должен прекращать работу и вернуть окончательную сумму.
# Напишите программу, которая будет использовать этот генератор для пошагового расчета суммы чисел, вводимых пользователем.

def sum_generator():
    summ = 0
    while True:
        new_value = yield summ
        if new_value is not None:
            summ += new_value


total_sum_calculator = sum_generator()

total_sum = 0
print('Введите числа для суммирования (0 для окончания):')
for total_sum in total_sum_calculator:
    user_value = int(input('Введите число: '))
    if user_value == 0:
        total_sum_calculator.close()
    else:
        total_sum_calculator.send(user_value)

print('Текущая сумма:', total_sum)


# 2. Напишите генератор, который будет генерировать арифметическую прогрессию

def arithmetic_progression_generator(start=1, step=1):
    while True:
        yield start
        start += step


arithmetic_progression = arithmetic_progression_generator(start=1, step=2)
for _ in range(5):
    print(next(arithmetic_progression), end=' ')
