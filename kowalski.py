import sys
import subprocess

#if (len(sys.argv) < 2):
#    print("ya burnt")
#    sys.exit(1)
#
#fileName = sys.argv[1]
#dumpFile = "~/Documents/school/cs239/dump.txt"
dumpFile = "dump.txt"


#cmdstring = "tshark -Y udp -nr " + fileName + " -T fields -e frame.len | sort -n | uniq -c > " + dumpFile

f=open(dumpFile, "r")
if f.mode == 'r':
    lines = f.read().splitlines()
    first = lines[0].strip().split(" ")
    last = lines[len(lines) - 1].strip().split(" ")
    print("Min="+first[1]+", Count=" + first[0])
    print("Max="+last[1]+", Count=" + last[0])
