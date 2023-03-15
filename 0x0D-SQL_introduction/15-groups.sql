-- lists the number of records with the same score in the table second_table
-- The result should display: the score
-- and the number of records for this score with the label number
-- The list is sorted by the number of records-descending
SELECT score, count(*) AS number FROM second_table
GROUP BY score ORDER BY score DESC;
