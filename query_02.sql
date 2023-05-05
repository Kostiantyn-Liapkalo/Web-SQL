-- 2 Знайти студента із найвищим середнім балом з певного предмета.
SELECT s.fullname, d.name, ROUND(AVG(g.grade), 2) AS average_mark
FROM grades AS g 
JOIN students AS s ON s.id = g.student_id 
JOIN disciplines AS d ON d.id = g.discipline_id 
WHERE d.id = 2
GROUP BY s.fullname, d.name
ORDER BY AVG(g.grade) DESC 
LIMIT 1;