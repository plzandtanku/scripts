#!/bin/bash

if [ -z "$1" ]
then
	echo "I NEED A FILE PLZ"
	exit
fi

echo "Processing: $1 ..."
for entry in $1/*
do
	my_arr=$(echo $entry | tr "/" "\n")
	for e in $my_arr
	do
		last=$e
	done
	/c/Program\ Files/Wireshark/tshark.exe -Y udp -nr $entry -T fields -e frame.len | sort -n | uniq -c > distributions/$last.txt
	/c/Program\ Files/Wireshark/tshark.exe -r $entry -q -z conv,udp > bitrates/$last-br.txt
	echo $last


done

#/c/Program\ Files/Wireshark/tshark.exe -Y udp -nr $1 -T fields -e frame.len | sort -n | uniq -c > dump.txt
#
#if [ ! -z "$2" ]
#then
#	/c/Program\ Files/Wireshark/tshark.exe -Y udp -nr $1 -T fields -e frame.len | sort -n | uniq -c > $2
#fi
#
#
#
#echo "Dropped contents into dump.txt"
#python kowalski.py
