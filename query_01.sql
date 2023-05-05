-- 1 Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.fullname, ROUND(AVG(g.grade), 2) AS average_mark
FROM students AS s 
JOIN grades AS g ON g.student_id = s.id
GROUP BY s.id 
ORDER BY AVG(g.grade) DESC 
LIMIT 5;
