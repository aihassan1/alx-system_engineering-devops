0x12-web_stack_debugging_2

Concepts:

Web stack debugging
User management
Running processes as different users
Nginx configuration
Requirements:

All files on Ubuntu 20.04 LTS
Files end with a newline
README.md file at the root
Bash scripts executable and pass Shellcheck
Scripts start with #!/usr/bin/env bash and comment explaining the purpose
Follow task instructions
Tasks:

1. Run software as another user (0-iamsomeoneelse):

Write a Bash script that accepts one argument (username).
Run whoami command as the provided user.
Test with different users. 2. Run Nginx as Nginx (1-run_nginx_as_nginx):

2. Run Nginx as Nginx (1-run_nginx_as_nginx):
   Ensure Nginx runs as the nginx user.
   Nginx listens on all active IPs on port 8080.
   Write a Bash script for configuration.
   Verify using ps auxff | grep ngin and nc -z 0 8080.
