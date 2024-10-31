-- Вывести население в каждой стране. Результат содержит два поля: CountryCode, sum(Population). Запрос по таблице city.
SELECT CountryCode, SUM(Population) 
FROM world.city c
GROUP BY CountryCode;

-- Изменить запрос выше так, чтобы выводились только страны с населением более 3 млн человек.
SELECT CountryCode, SUM(Population) sum_population
FROM world.city c
GROUP BY CountryCode
HAVING sum_population > 3000000

-- Поменять запрос выше так, чтобы в результате вместо кода страны выводилось ее название. Подсказка: нужен join таблиц city и country по полю CountryCode.
SELECT co.Name , SUM(ci.Population) sum_population
FROM world.city ci
INNER JOIN world.country co ON co.Code = ci.CountryCode 
GROUP BY CountryCode
HAVING sum_population > 3000000

-- Вывести количество городов в каждой стране (CountryCode, amount of cities). Подсказка: запрос по таблице city и группировка по CountryCode.
SELECT CountryCode, SUM(c.id) amount_of_cities
FROM world.city c
GROUP BY CountryCode;

-- Поменять запрос так, чтобы вместо кодов стран, было названия стран.
SELECT co.Name , SUM(ci.id) amount_of_cities
FROM world.city ci
INNER JOIN world.country co ON co.Code = ci.CountryCode 
GROUP BY CountryCode

-- Поменять запрос так, чтобы выводилось среднее количество городов в стране.
-- Подсказка: разделите задачу на несколько подзадач. Например, сначала вывести код страны и количество городов в каждой стране.  Затем сделать join получившегося результата с запросом, где высчитывается среднее от количества городов. Потом добавить join, который добавит имена стран, вместо кода.

