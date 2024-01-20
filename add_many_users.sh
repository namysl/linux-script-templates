#!/bin/bash

#list of users
userfile=/tmp/uzytkownicy

username=$(cat /tmp/uzytkownicy | tr 'A-Z' 'a-z')

#temp password
password=" "
group=uzyszkodnicytest
groupadd $group

for user in $username
do
  useradd $user
  #another option
  #echo $user:$password | chpasswd
  echo $password | passwd $user --stdin
  usermod -a -G $group $user
done

echo "$(wc -l /tmp/uzytkownicy) users have been created"
tail -n $(wc -l /tmp/uzytkownicy) /etc/passwd  