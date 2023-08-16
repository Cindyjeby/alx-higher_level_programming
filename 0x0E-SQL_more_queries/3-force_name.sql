-- Script that creates the table force_nmame on the MySQL server
-- Description: id=INT, name=VARCHAR(256) can not be null
-- If the tables already exists the script should not fail
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
	);
