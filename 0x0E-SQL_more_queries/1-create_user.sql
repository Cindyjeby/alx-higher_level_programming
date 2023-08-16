--Script that creates the MySQL server user User_0d_1
--the user password should be set to user_0d_1_pwd
--if the user already exists the script shouldnot fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_od_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
