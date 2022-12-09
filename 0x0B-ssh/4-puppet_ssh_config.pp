# config ssh_config
file_line {'pass auten No':
  ensure => present,
    path => '/etc/ssh/ssh_config',
    line => ' PasswordAuthentication no',
    match=> 'PasswordAuthentication yes',
}
file_line {'Add ident file':
  ensure => present,
    path => '/etc/ssh/ssh_config',
    line => ' IdentityFile ~/.ssh/holberton',
}
