--script that creates the database hbtn_0d_02 and the user_0d_2
--user should have only SELECT priviledge in the datatbase
--user passward should be set to user_0d_2_pwd
--if database already exists the script should not fail
--if the user already exists the script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbnt_0d_2.* TO 'user_0d_2'@'localhost';
