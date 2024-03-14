# nginx_config.pp

# Define an exec resource to replace the line that starts with 'worker_processes' using sed
exec { 'set_worker_processes':
  command  => "sed -i 's/^worker_processes\\s\\+\\d\\+;/worker_processes 14;/' /etc/nginx/nginx.conf",
  provider => shell,
}

# Define an exec resource to uncomment the 'multi_accept' directive using sed
exec { 'enable_multi_accept':
  command  => "sed -i 's/^#\\s*multi_accept\\s*on;/multi_accept on;/' /etc/nginx/nginx.conf",
  provider => shell,
}


