`sudo adduser ali` to add a user named ali
`su ali` to login as ali
`deluser ali --remove-home` delete user ali and it's home directory
`sudo addgroup students` add students group in the /etc/group dir
`gpasswd -d ali students` add ali to students group
`sudo delgroup students` delete students group
`chmod [ugoa][-+=][rwx] file` change permission to file

for file types in linux permissions you have d for directory, l for link, c for character, b for block and - for file