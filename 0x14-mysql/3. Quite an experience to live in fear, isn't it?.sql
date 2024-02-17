-- Connect to your MySQL server as a privileged user (e.g., root)
sudo mysql

-- Create replica_user with appropriate permissions
CREATE USER 'replica_user'@'%' IDENTIFIED WITH mysql_native_password BY '1234';

-- Grant replication permissions to replica_user
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'replica_user'@'%';

-- Ensure that holberton_user has SELECT privileges on the mysql.user table
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

-- Exit from MySQL shell
exit


CHANGE MASTER TO MASTER_HOST='18.210.14.47',
MASTER_USER='replica_user', MASTER_PASSWORD='1234', 
MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=101;
