#!/bin/bash

if [ $# -lt 1 ]; then
	while true
		do
		time=$(TZ='Europe/Oslo' date +%T)
		echo "NORWEGIAN TIME: $time"
		sleep 1

option=$1;
if [ "$option" == "no" ]; then # no = Norway
	while true
		do
		clear
		timeNO=$(TZ='Europe/Oslo' date +%T)
		echo "NORWEGIAN TIME: $timeNO"
		sleep 1
		done

elif [ "$option" == "sk" ]; then
	while true
		do
		timeSK=$(TZ='Asia/Seoul' date +%T)
		clear
		echo "SOUTH KOREAN TIME: $timeSK"
		sleep 1
		done
elif [ "$option" == "us" ]; then
	while true
		do
		timeUS=$(TZ='America/New_York' date +%T)
		clear
		echo "NEW YORK TIME $timeUS"
		sleep 1
		done
else
	echo "Insert city 'no':Norway-Oslo, 'sk':South_Korea-Seoul or 'us':United_States-New_York";
	exit 0
fi

