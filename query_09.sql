-- 9 Знайти список курсів, які відвідує студент.
SELECT s.fullname AS student, d.name AS discipline
FROM grades AS g
LEFT JOIN students AS s ON s.id = g.student_id
LEFT JOIN disciplines AS d ON d.id = g.discipline_id
WHERE s.id = 9
GROUP BY d.id, s.fullname;