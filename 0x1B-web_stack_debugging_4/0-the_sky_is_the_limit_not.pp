# nginx_config.pp

# Define an exec resource to replace the line that starts with 'worker_processes' using sed
exec { 'change_ulimit':
  command  => "sed -i 's/ULIMIT=\"-n [0-9]*\"/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  provider => shell,
}


# Define an exec resource to restart the Nginx service
exec { 'restart_nginx':
  command  => 'service nginx restart',
  provider => shell,
  require  => [Exec['change_ulimit']],
}
