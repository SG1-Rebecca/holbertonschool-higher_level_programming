-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if it does not exist and set password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT in the entire hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';