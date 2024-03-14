# Define a file resource to manage the limits.conf file

exec { 'remove_holberton_limits':
  command  => "sed -i '/^holberton/d' /etc/security/limits.conf",
  provider => shell,
}
