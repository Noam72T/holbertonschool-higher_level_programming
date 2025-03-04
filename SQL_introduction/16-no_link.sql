-- lists all records with a name value


-- Select the score and name from the second_table where the name is not NULL
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
