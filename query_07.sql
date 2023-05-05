-- 7 Знайти оцінки студентів у окремій групі з певного предмета.
SELECT gr.name AS Group_Name, s.fullname AS student, d.name AS subject, g.grade AS mark
FROM grades AS g
LEFT JOIN students AS s ON s.id  = g.student_id 
JOIN disciplines AS d ON d.id = g.discipline_id 
LEFT JOIN groups AS gr ON gr.id = s.group_id
WHERE gr.id = 3 AND d.id = 3
ORDER BY s.fullname DESC;