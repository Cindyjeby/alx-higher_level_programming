-- Script that creates the database hbtn_0d_usa and the table states on the MySQL server
-- Description: id= INT unidue, auto generated, cant be null and is a primary key, name=VARCHAR(256)cant be null
-- If the database or thr table already exists the script shouldnot fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);
