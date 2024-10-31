-- Найдите самого старшего студента
SELECT *
FROM Students.Students s 
ORDER BY age DESC 
LIMIT 1;

-- Найдите самого старшего преподавателя
SELECT *
FROM Students.Teachers t
WHERE t.age = (SELECT MAX(age) FROM Students.Teachers)
LIMIT 1;

-- Выведите список преподавателей с количеством компетенций у каждого
SELECT t.*, COUNT(tc.competencies_id) competencies_count
FROM Students.Teachers t 
LEFT JOIN Students.Teachers2Competencies tc ON tc.teacher_id = t.id 
GROUP BY t.id 

-- Выведите список курсов с количеством студентов в каждом
SELECT c.*, COUNT(sc.id) students_count
FROM Students.Courses c 
LEFT JOIN Students.Students2Courses sc ON sc.course_id = c.id
GROUP BY c.id 

-- Выведите список студентов, с количеством курсов, посещаемых каждым студентом. 
SELECT s.*, COUNT(sc.id) courses_count
FROM Students.Students s
LEFT JOIN Students.Students2Courses sc ON sc.student_id = s.id
GROUP BY s.id 