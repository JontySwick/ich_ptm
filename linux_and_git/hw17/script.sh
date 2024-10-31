#!/bin/bash

read -p "Enter destination for ping: " address

fail_count=0
while true
do
	ping_result=$(ping -c 1 "$address")
	if [[ $? -ne 0 ]]; then
		((fail_count++))
	else
		fail_count=0
		avg_time=$(echo "$ping_result" | tail -n 1 | awk -F '/' '{print $5}')

		if [[ $(echo "$avg_time > 100" | bc -l) -eq 1 ]]; then
			$fail_count=3
		fi
	fi

	if [[ $fail_count -ge 3 ]]; then
		echo "Bad connection with $address"
	fi

	sleep 1
done
