-- Create a new database 
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create a new user with password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privileges to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';