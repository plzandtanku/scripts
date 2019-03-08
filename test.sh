#!/bin/bash

if [ -z "$1" ]
then
	echo "I NEED A FILE PLZ"
	exit
fi
echo "Processing: $1 ..."
/c/Program\ Files/Wireshark/tshark.exe -Y udp -nr $1 -T fields -e frame.len | sort -n | uniq -c > dump.txt

echo "Dropped contents into dump.txt"
python kowalski.py
