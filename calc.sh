#!/bin/bash

#Creating a Calculator in Bash script

if (( $# ==0 )); then
	echo "Supply with arguments 'S':sum, 'P':product, 'M':max or 'm':min."
	exit 0

elif (( $# ==1 )); then
	echo "Error message, no numbers are supplied."
	exit 0
else
	option=$1; #load cmd-line arg into option
	shift;

	if [ "$option" == "S" ]; then # Sum all arguments after the first cmd-arg
		sum=0
		for i in $@; do sum=$((sum+i)); done
			echo "$sum"
			exit 0

	elif [ "$option" == "P" ]; then # product of all arguments after the first arg
		product=1
		for i in $@; do product=$((product*i)); done
			echo "$product"
			exit 0

	elif [ "$option" == "M" ]; then # find the max value of the cmd-line args.
		maxVal=$1
		for i in $@; do
			if (( $i > $maxVal )); then
				maxVal="$i"; fi;
		done
		echo "$maxVal"
		exit 0

	elif [ "$option" == "m" ]; then # find the minimum value of the cmd-line args.
		minVal=$1
		for i in $@; do
			if (( $i < $minVal )); then
				minVal="$i"; fi;
		done
		echo "$minVal"
		exit 0
	else
		echo exit;
	fi
fi
