-- 4 Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT ROUND(AVG(g.grade), 2) AS average_mark
FROM grades AS g;
