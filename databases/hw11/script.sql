-- Вывести список region_id, total_countries, где total_countries - количество стран в таблице. 
-- Подсказка: работаем с таблицей countries, использовать оконную функцию over() и суммировать count(country_id).
SELECT region_id, COUNT(country_id) OVER() total_countries
FROM hr.countries c ;

-- Изменить запрос 2 таким образом, чтобы для каждого region_id выводилось количество стран в этом регионе. Подсказка: добавить partition by region_id в over().
SELECT region_id, COUNT(country_id) OVER(PARTITION BY region_id) total_countries
FROM hr.countries c ;

-- Работа с таблицей departments. Написать запрос, который выводит location_id, department_name, dept_total, где dept_total - количество департаментов в location_id.
SELECT location_id, department_name, COUNT(department_id) OVER(PARTITION BY location_id) dept_total
FROM hr.departments d 

-- Изменить запрос 3 таким образом, чтобы выводились названия городов соответствующих location_id.
SELECT l.city, d.department_name, COUNT(d.department_id) OVER(PARTITION BY d.location_id) dept_total
FROM hr.departments d 
INNER JOIN hr.locations l ON l.location_id = d.location_id 

-- Работа с таблицей employees. Вывести manager_id, last_name, total_manager_salary, где total_manager_salary - общая зарплата подчиненных каждого менеджера (manager_id).
SELECT manager_id, last_name, SUM(salary) OVER(PARTITION BY manager_id) total_manager_salary
FROM hr.employees e 