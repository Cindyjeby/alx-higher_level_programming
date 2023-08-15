-- Script that lists the number of records with the same score in the table second_table
-- Results shold display, the score, the number of the records for this score with the label number
-- The list should be sorted by the number of records(descening)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
