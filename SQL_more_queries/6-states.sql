-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on my MySQL server

-- Create the database if it doesn't exist already
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the table states if it doesn't exist already
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
