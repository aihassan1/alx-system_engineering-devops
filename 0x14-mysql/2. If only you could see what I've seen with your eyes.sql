-- Connect to MySQL and create the database tyrell_corp
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- Switch to the tyrell_corp database
USE tyrell_corp;

-- Create a table named nexus6 within the tyrell_corp database
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

-- Insert at least one entry into the nexus6 table
INSERT INTO nexus6 (name) VALUES ('Abdelrahman');

-- Grant SELECT permissions on the nexus6 table to the user replica_user.
-- GRANT SELECT ON tyrell_corp.nexus6 TO 'replica_user'@'localhost';
