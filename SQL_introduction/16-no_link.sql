-- List all records of 'second_table' of db 'hbtn_0c_0'
SELECT score, name FROM second_table
WHERE name is NOT NULL
ORDER BY score DESC;
