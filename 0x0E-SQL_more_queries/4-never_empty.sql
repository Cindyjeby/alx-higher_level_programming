-- Script that creates the table id_not_null on the My SQL server
-- Description: id=INT with the default value 1, name=VARCHAR(256)
-- If the table already exists the script shoulf not fail

CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
