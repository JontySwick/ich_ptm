-- Вывести текущую дату и время.
SELECT NOW();

-- Вывести текущий год и месяц
SELECT DATE_FORMAT(NOW(), '%Y %m');

-- Вывести текущее время
SELECT DATE_FORMAT(NOW(), '%H:%i');

-- Вывести название текущего дня недели
SELECT DATE_FORMAT(NOW(), '%W');

-- Вывести номер текущего месяца
SELECT DATE_FORMAT(NOW(), '%m');

-- Вывести номер дня в дате “2020-03-18”
SELECT DATE_FORMAT('2020-03-18', '%d');

-- Подключиться к базе данных shop (которая находится на удаленном сервере).
-- Определить какие из покупок были совершены апреле (4-й месяц)
SELECT *
FROM shop.ORDERS o 
WHERE DATE_FORMAT(o.ODATE, '%m') = 4;

-- Определить количество покупок в 2022-м году
SELECT COUNT(*)
FROM shop.ORDERS o 
WHERE DATE_FORMAT(o.ODATE, '%Y') = 2022;

-- Определить, сколько покупок было совершено в каждый день. Отсортировать строки в порядке возрастания количества покупок. Вывести два поля - дату и количество покупок
SELECT o.ODATE, COUNT(*)
FROM shop.ORDERS o
GROUP BY o.ODATE;

-- Определить среднюю стоимость покупок в апреле
SELECT AVG(o.AMT) 
FROM shop.ORDERS o 
WHERE DATE_FORMAT(o.ODATE, '%m') = 4;