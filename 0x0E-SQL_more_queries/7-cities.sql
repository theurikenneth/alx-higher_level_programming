-- Creates the database htbn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on my MySQL server.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the new table
USE hbtn_0d_usa;
-- create states table
CREATE TABLE IF NOT EXISTS cities (
       id INT UNIQUE AUTO_INCEREMENT NOT NULL,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL, PRIMARY KEY (id),
       CONSTRAINT cities_ibfk_1 FOREIGN KEY (state_id) REFERENCES states(id)
);
