#!/bin/bash

for i in $(cat servers) ;
  do
    ping -c 1 $i
    echo "================="
  done 