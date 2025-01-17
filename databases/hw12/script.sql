-- 1. Вывести количество городов для каждой страны. Результат должен содержать CountryCode, CityCount (количество городов в стране).
-- Поменяйте запрос с использованием джойнов так, чтобы выводилось название страны вместо CountryCode.
SELECT c.Name, count(ci.ID) as CityCount
FROM world.city as ci
INNER JOIN world.country c ON ci.CountryCode = c.Code
GROUP BY c.Name;

-- 2. Используя оконные функции, вывести список стран с продолжительностью жизнью и средней продолжительностью жизни.
SELECT Name, LifeExpectancy, avg(LifeExpectancy) OVER() AvgLifeExpectancy
FROM world.country;

-- 3. Используя ранжирующие функции, вывести страны по убыванию продолжительности жизни.
SELECT Name, LifeExpectancy, DENSE_RANK() OVER (ORDER BY LifeExpectancy DESC ) LifeExpectancyRank
FROM world.country;

-- 4. Используя ранжирующие функции, вывести третью страну с самой высокой продолжительностью жизни.
SELECT *
FROM (
	SELECT Name, LifeExpectancy, DENSE_RANK() OVER (ORDER BY LifeExpectancy DESC ) LifeExpectancyRank
	FROM world.country
) as sub_query
WHERE LifeExpectancyRank = 3;