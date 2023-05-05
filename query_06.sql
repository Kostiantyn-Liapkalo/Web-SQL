-- 6 Знайти список студентів у певній групі.
SELECT g.name, s.fullname
FROM students AS s
LEFT JOIN groups AS g ON g.id = s.group_id 
WHERE g.id = 1;