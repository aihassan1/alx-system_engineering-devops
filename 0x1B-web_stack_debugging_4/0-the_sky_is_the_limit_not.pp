# nginx_config.pp

# Define an exec resource to replace the line that starts with 'worker_processes' using sed
exec { 'set_worker_processes':
  command  => "sed -i 's/[[:space:]]*worker_processes [0-9]*;/worker_processes 14;/' /etc/nginx/nginx.conf",
  provider => shell,
}

# Define an exec resource to uncomment the 'multi_accept' directive using sed
exec { 'enable_multi_accept':
  command  => "sed -i 's/[[:space:]]*#\\s*multi_accept\\s*on;/multi_accept on;/' /etc/nginx/nginx.conf",
  provider => shell,
}

# Define an exec resource to restart the Nginx service
exec { 'restart_nginx':
  command  => 'service nginx restart',
  provider => shell,
  require  => [Exec['set_worker_processes'], Exec['enable_multi_accept']],
}
