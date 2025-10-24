-- Create the database 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Move to the newly created database
USE hbtn_0d_usa;

-- Create the table
CREATE TABLE IF NOT EXISTS states(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);