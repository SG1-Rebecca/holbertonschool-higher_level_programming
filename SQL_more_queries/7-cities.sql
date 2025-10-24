-- Create the database 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Move to the newly created database
USE hbtn_0d_usa;

-- Create the table with foreign key
CREATE TABLE IF NOT EXISTS cities(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);