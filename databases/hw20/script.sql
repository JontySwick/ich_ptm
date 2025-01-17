-- 1. Подключитесь к базе данных hr (которая находится на удаленном сервере).
USE hr;

-- 2. Выведите количество сотрудников в базе
SELECT COUNT(*)
FROM employees;

-- 3. Выведите количество департаментов (отделов) в базе
SELECT COUNT(*)
FROM departments;

-- 4. Подключитесь к базе данных World (которая находится на удаленном сервере).
use world;

-- 5. Выведите среднее население в городах Индии (таблица City, код Индии - IND)
SELECT AVG(Population) avg_pop
FROM city
WHERE CountryCode = 'IND';

-- 6. Выведите минимальное население в индийском городе и максимальное.
SELECT MIN(Population), MAX(Population)
FROM city
WHERE CountryCode = 'IND';


-- 7. Выведите самую большую площадь территории.
SELECT MAX(SurfaceArea)
FROM country;

-- 8. Выведите среднюю продолжительность жизни по странам.
SELECT Name, LifeExpectancy
FROM country;

-- 9. Найдите самый населенный город (подсказка: использовать подзапросы)
SELECT *
FROM city
WHERE Population = (SELECT MAX(Population) FROM city)


