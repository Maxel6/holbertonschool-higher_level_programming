-- List number of records with same score in 'second_table' of db 'hbtn_0c_0'
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
