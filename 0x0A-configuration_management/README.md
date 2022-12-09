## CONFIGURATION MANAGEMENT

File | Description
---- | -----------
[0-create_a_file.pp](./0-create_a_file.pp) | Creates a file /tmp using puppet whith the following requirements: File path /tmp/school <br> File permission is 0744 <br> File owrner is www-data <br> File group is www-data <br> File contains I love puppet
[1-install_a_package.pp](./1-install_a_package.pp) | Installs flast from pip3 using puppet. Flast version should be 2.1.0
[2-execute_a_command.pp](./2-execute_a_command.pp) | Creates a manifest that kills process named 'killmenow' using puppet
