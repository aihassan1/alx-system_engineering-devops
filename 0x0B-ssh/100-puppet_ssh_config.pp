# 100-puppet_ssh_config.pp

file_line { 'Declare_identity_file':
  path => '/etc/ssh/ssh_config', 
  line => 'IdentityFile ~/.ssh/school',
}

file_line { 'Turn_off_password_authentication':
  path => '/etc/ssh/ssh_config',  
  line => 'PasswordAuthentication no',
}
