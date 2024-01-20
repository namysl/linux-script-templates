#!/bin/bash

for serw in $(cat lista_serw) ;
do
  echo $serw ; sshpass -p " " ssh -o StrictHostKeyChecking=no me@$serw "uptime"
done