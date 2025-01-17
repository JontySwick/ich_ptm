1. Давайте создадим простой калькулятор. Напишите программу, которая запрашивает у пользователя два целых числа и выполняет следующие действия:

   - Вычисляет сумму и выводит результат.

   - Вычисляет разность и выводит результат (первое число минус второе число).

   - Вычисляет произведение и выводит результат.

   - Вычисляет частное (результат деления первого числа на второе) и выводит результат.

   - Вычисляет остаток от деления первого числа на второе и выводит результат.

   - Возводит первое число в степень второго числа и выводит результат.

    Пример вывода:

    ```console
    Введите первое число: 5
    Введите второе число: 2
    Сумма: 7
    Разность: 3
    Произведение: 10
    Частное: 2.5
    Остаток от деления: 1
    Первое число в степени второго числа: 25
    ```

2. Есть круглая арена цирка, нам известен ее радиус, нужно подобрать покрытие для этой арены, чтобы это сделать необходимо узнать длину и площадь окружности. Напишите программу, которая запрашивает у пользователя радиус окружности и выполняет следующие действия:

   - Вычисляет длину окружности по формуле 2 * pi * r, где pi – математическая константа (примерно равна 3.14159), а r – радиус окружности. Выводит результат.

   - Вычисляет площадь окружности по формуле pi * r^2, где pi – математическая константа, а r – радиус окружности. Выводит результат.

    ```console
    Пример вывода:
    Введите радиус окружности: 4.5
    Длина окружности: 28.274333882308138
    Площадь окружности: 63.61725123519331
    ```
   
3. Географ хочет находить расстояние между двумя точками на карте. Напишите для него программу, которая запрашивает у пользователя координаты двух точек в двумерном пространстве (x1, y1) и (x2, y2), а затем вычисляет и выводит расстояние между этими точками по формуле:

    distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

   где sqrt - функция извлечения квадратного корня. Не используйте встроенную математическую функцию sqrt для вычисления корня. Не забывайте, что sqrt(x)==x**0.5. Результат должен быть выведен с помощью команды print.

    Пример вывода:
    
    ```console
    Введите координаты первой точки (x1, y1): 2, 3
    Введите координаты второй точки (x2, y2): 5, 7
    Расстояние между точками: 5.0
   ```