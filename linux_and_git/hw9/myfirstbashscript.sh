#!/bin/bash

date

echo "hello $USER!"

pwd

ps awx | grep "bioset" | grep -v -c "grep"

ls -l /etc/passwd | awk  -F' ' '{print $1}'
