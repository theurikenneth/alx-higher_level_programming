-- Creates a table 'second_table' in the
-- databse 'hbtn_0c_0' in MySQL Server and
-- adds multiple rows.

CREATE TABLE IF NOT EXISTS second_table (
       id INT,
       name VARCHAR(256),
       score INT
);
-- adding some data
INSERT INTO second_table
VALUES
(1, "John", 10);
(2, "Alex", 3);
(3, "Bob", 14);
(4, "George", 8);
