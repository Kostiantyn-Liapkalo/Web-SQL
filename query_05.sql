-- 5 Знайти які курси читає певний викладач.
SELECT t.fullname, d.name  
FROM disciplines AS d 
LEFT JOIN teachers AS t ON t.id = d.teacher_id 
WHERE t.id = 2;