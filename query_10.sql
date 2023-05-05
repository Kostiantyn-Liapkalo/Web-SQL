-- 10 Список курсів, які певному студенту читає певний викладач.
SELECT d.name AS subject, s.fullname AS student, t.fullname AS teacher 
FROM grades AS g 
LEFT JOIN disciplines AS d ON d.id = g.discipline_id 
LEFT JOIN teachers AS t ON t.id = g.discipline_id
LEFT JOIN students AS s ON s.id = g.student_id
WHERE s.id = 1 AND t.id = 3
GROUP BY d.id, s.fullname, t.fullname;