# Define a file resource to manage the limits.conf file

exec { 'change_soft_limit':
    
    command  => "sed -i 's/holberton hard nofile [0-9]*/holberton hard nofile 1024' /etc/security/limits.conf",
    provider => shell,
}

exec { 'change_ulimit':
  command  => "sed -i 's/holberton soft nofile [0-9]*/holberton soft nofile 1024' /etc/security/limits.conf",
  provider => shell,
}
