-- Script that converts hbtn_0c_0 database to UTF8
-- To be converted: database=hbtn_0c_0, table=first_table, field name in first_table
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
