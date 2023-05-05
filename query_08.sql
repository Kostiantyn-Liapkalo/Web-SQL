-- 8 Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.fullname  AS teacher , ROUND(AVG(g.grade),2) AS average_mark
FROM disciplines d 
LEFT JOIN grades g ON g.discipline_id = d.id 
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 4
group by t.fullname;