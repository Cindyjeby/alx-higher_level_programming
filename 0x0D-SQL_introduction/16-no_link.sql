-- Script that lists all records of the table second_table
-- Donot list rows without a name Value
-- Results should display the score and the name(in this order)
-- Records should be listed by decending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
