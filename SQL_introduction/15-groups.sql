-- lists the number of records with the same score in the second_table

-- Select the score and the number of records for each score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
