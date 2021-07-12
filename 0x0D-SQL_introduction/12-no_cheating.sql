-- Updates the score of the record in the
-- table 'second_table' in MySQL Server
-- using the name not the id
UPDATE second_table
SET 'score' = '10'
WHERE 'name' = 'Bob';
