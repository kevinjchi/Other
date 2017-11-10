#!/bin/bash
#Creating a bookmarker in bash

bookmarkFile=~/.bookmarks
#create bookmarksFile if it does not exits
if [ ! -f $bookmarkFile ]; then
#	echo "bookmarkFile not found, creating a file"
	touch $bookmarkFile
fi

if [ $# -ge 1 ] && [ $# -le 2 ]; then
	option=$1; #this cmd-line argument should be '-r' or '-a'
	if [ "$option" == "-a" ]; then
		if [ $# -eq 1 ]; then
			echo "Error: You forgot to supply the bookmarkname to add"
		elif [ $# -eq 2 ]; then
			bookmarkname=$2
			bookmarklocation=$(pwd)
			echo "$bookmarkname|$bookmarklocation" >> $bookmarkFile
		fi
	elif [ "$option" == "-r" ]; then
		if [ $# -eq 1 ]; then
			echo "Error: You forgot to supply the bookmarkname to remove"
		elif [ $# -eq 2 ]; then
			bookmarkname=$2
			bookmarklocation=$(pwd)
			sed -i "s/\<$bookmarkname\>//g" $bookmarkFile
			sed -i "/^|/d" $bookmarkFile
			unset "$bookmarkname"
		fi
	else
		echo "ERROR: Please write '-a' or '-r' as the first cmd-line argument, your current argument is invalid."
	fi

elif [ $# -gt 2 ]; then
	echo "ERROR: Too many arguments."
fi

if [ -f $bookmarkFile ]; then
	declare -a array
	readarray -t array < $bookmarkFile
	for i in ${array[@]}; do
		bookmarknumber=$i
		bookmarkname=${bookmarknumber%|*} #everything before name
		bookmarklocation=${bookmarknumber#*|} #everything after name
		export $bookmarkname=$bookmarklocation
	done
fi
