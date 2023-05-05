-- 3 Знайти середній бал у групах з певного предмета.
SELECT g2.name, d.name, ROUND(AVG(g.grade), 2)
FROM grades g 
LEFT JOIN students AS s ON s.id  = g.student_id 
LEFT JOIN disciplines AS d ON d.id = g.discipline_id 
LEFT JOIN groups AS g2 ON g2.id = s.group_id
WHERE d.id = 1
GROUP BY g2.id, d.name
ORDER BY AVG(g.grade) DESC;