-- List all records in the table second_table with a score >= 10 in MySQL server.
-- Records should be ordered by score(top first).
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
