#!/bin/bash
set -e

mkdir -p ./even_files ./odd_files

for i in {1..100}
do
	file_name=$RANDOM
	touch ./odd_files/$file_name
	if (( $file_name % 2 == 0 )); then
		mv ./odd_files/$file_name ./even_files/
	fi
done
