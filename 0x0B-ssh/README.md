## SSH
File | Description
---- | -----------
[0-use_a_private_key](./0-use_a_private_key) | Bash script that uses 'ssh' to connevt to server using private key '`/.ssh/school' with user 'ubuntu'
[1-create_ssh_key_pair](./1-create_ssh_key_pair) | Bash script that creates an RSA key pair
[2-ssh_config](./2-ssh_config) | File that configures local SSH Client in order to connect to server without typing a password
[100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp) | Script that set up your client SSH configuration file so that you can connect to a server without typing a password.
