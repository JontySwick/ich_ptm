# 1.  Даны формулы: ¬((A ∨ B) ∧ (C ∨ D)) и ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D)). Используя закон Де Моргана, докажите,
# что эти формулы эквивалентны.
# ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D)) = (¬(A ∨ B) ∨ ¬(C ∨ D)) = ¬((A ∨ B) ∧ (C ∨ D))

# Напишите программу, которая запрашивает у пользователя два логических значения (True или False) и выводит
# результаты следующих логических операций
first_variable = input('Enter first boolean variable ("y" for True, any other symbol for False): ').lower() == 'y'
second_variable = input('Enter second boolean variable ("y" for True, any other symbol for False): ').lower() == 'y'

print(
    'Результат логического И: ' + ('True' if first_variable and second_variable else 'False'),
    'Результат логического ИЛИ: ' + ('True' if first_variable or second_variable else 'False'),
    'Результат логического НЕ (для первого значения): ' + ('True' if not first_variable else 'False'),
    'Результат логического НЕ (для второго значения): ' + ('True' if not second_variable else 'False'),
    'Результат сравнения на равенство: ' + ('True' if first_variable == second_variable else 'False'),
    'Результат сравнения на неравенство: ' + ('True' if first_variable != second_variable else 'False'),
    sep='\n'
)
