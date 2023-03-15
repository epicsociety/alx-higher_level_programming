-- lists all records of the table second_table of db hbtn_0c_0
-- records are sort by score in a descending order, where score >= 10
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
