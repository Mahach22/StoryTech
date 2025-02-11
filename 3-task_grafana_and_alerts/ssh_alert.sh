#!/bin/bash

USER=$1
IP=$2
DATE=$(date +"%Y-%m-%d %H:%M:%S")
HOSTNAME=$(hostname)

SUBJECT="SSH Alert: User $USER logged in from $IP on $HOSTNAME"
BODY="User: $USER\nIP Address: $IP\nDate: $DATE\nHostname: $HOSTNAME"

echo -e "$BODY" | mail -s "$SUBJECT" -r gad000@bk.ru mahach2211@gmail.com
