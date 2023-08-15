-- Script that creates a table second_table in the database hbtn_0c_0 in the MySQL server and adds multiple rows
-- Description: id=INT, name=VARCHAR(256), score=INT
-- script should create the following records: (id=1, name=john, score=10), (id=2, name=alex, score=3), (id=3 name=bob, score=14), (id=4 name=george, score=8)
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT
	);
	INSERT INTO second_table (id, name, score) VALUES (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);
