-- 11 Середній бал, який певний викладач ставить певному студентові.
SELECT t.fullname AS TEACHER, s.fullname AS STUDENT, ROUND(AVG(g.grade), 2) AS AVERAGE_MARK
FROM grades AS g
LEFT JOIN disciplines AS d ON d.id = g.discipline_id 
LEFT JOIN teachers AS t ON t.id = d.teacher_id 
LEFT JOIN students AS s ON s.id  = g.student_id
WHERE s.id = 4 AND t.id = 3
GROUP BY t.fullname, s.fullname;