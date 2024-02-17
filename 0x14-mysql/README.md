0x14-mysql

Project Overview:

This project focuses on DevOps, SysAdmin, and MySQL administration skills.
You'll gain hands-on experience with:
Installing and configuring MySQL 5.7.x on Ubuntu 16.04 LTS servers.
Setting up primary-replica database clusters for redundancy and load balancing.
Creating and managing MySQL users and databases.
Implementing essential security measures.
Performing regular backups and storing them in separate locations.
Requirements:

Access to two Ubuntu 16.04 LTS servers with internet connectivity.
Familiarity with Linux basics, Bash scripting, and MySQL concepts.
Adherence to project-specific rules, including:
Using vi, vim, or emacs editors.
Following naming conventions and code styling guidelines.
Passing Shellcheck (version 0.3.7-5~ubuntu16.04.1).
Providing comments in your scripts.
Tasks:

1. Install MySQL (0.0%):

Install MySQL 5.7.x on both web-01 and web-02 servers.
Ensure task #3 of your SSH project is completed for both servers.
Check mysql --version to confirm installation.
2. Let us in! (0.0%):

Create holberton_user (localhost, projectcorrection280hbtn password) on both servers.
Grant SELECT permissions on the replication status tables.
Ensure task #3 of your SSH project is completed for both servers.
Check mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'".
3. If only you could see what I've seen with your eyes (0.0%):

Create the tyrell_corp database and nexus6 table with at least one entry on web-01.
Grant SELECT permissions on nexus6 to holberton_user.
Check mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6".
4. Quite an experience to live in fear, isn't it? (0.0%):

Create replica_user (% hostname, custom password) on web-01 with replication privileges.
Grant SELECT on mysql.user to holberton_user.
Check mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'.
5. Setup a Primary-Replica infrastructure using MySQL (0.0%):

Configure web-01 as the primary (no bind-address), web-02 as the replica.
Configure replication for tyrell_corp database.
Provide MySQL configuration files:
4-mysql_configuration_primary
4-mysql_configuration_replica
Verify replication by adding a record on web-01 and checking web-02.
Ensure UFW allows connections on port 3306.
6. MySQL backup (0.0%):

Write a Bash script to:
Dump all MySQL databases using mysqldump and root credentials (provided as an argument).
Compress the dump to a day-month-year.tar.gz archive.
Test the script with a valid password (./5-mysql_backup mypassword).
Additional Notes:

Remember to replace placeholders like usernames, passwords, and IP addresses with your actual values.
Follow best practices for database security, data privacy, and system hygiene.
Document your changes clearly in the README and any scripts.
Test your configurations thoroughly to ensure functionality and reliability.
