```
enable
configure terminal
hostname <hostname>
enable secret password
line console 0
password <password>
login
line vty 0 4
password <password>
login
transport input all
exit
service password-encryption
banner motd <delmiter> <message> <delimiter>
copy running-config startup-config
```
