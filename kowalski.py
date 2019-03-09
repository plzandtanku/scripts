import os
import sys

myDir = None
if (len(sys.argv) > 1):
    myDir = sys.argv[1]
   #if (len(sys.argv) < 2):
#    print("ya burnt")
#    sys.exit(1)
#
#fileName = sys.argv[1]
#dumpFile = "~/Documents/school/cs239/dump.txt"
d = "dump.txt"


#cmdstring = "tshark -Y udp -nr " + fileName + " -T fields -e frame.len | sort -n | uniq -c > " + dumpFile
def analyzeFile(dumpFile):
    f=open(dumpFile, "r")
    if f.mode == 'r':
        lines = f.read().splitlines()
        first = lines[0].strip().split(" ")
        last = lines[len(lines) - 1].strip().split(" ")
        print("Min="+first[1]+", Count=" + first[0])
        print("Max="+last[1]+", Count=" + last[0])
        total = 0
        for line in lines:
            count = line.strip().split(" ")[0]
            total += int(count)
        print ("Num Packets=" + str(total))


def readConv(fileName):
    f=open(fileName, "r")
    if f.mode == 'r':
        lines = f.read().splitlines()
        for line in lines:
            arr = line.split()
            print(arr)
readConv(d)
sys.exit(1)
if (myDir is None):
    print("analyzing single file")
    analyzeFile(d)
else:
    dic={"maxSize":0, "fileName":""}
    dic2={"mostP":0,"fileName":""}
    dic3={"minSize":-1,"fileName":""}
    for f in os.listdir(myDir):
        if (len(f.split(".")) > 1 and f.split(".")[len(f.split("."))-1] == 'txt'):
            fil=open(myDir+f, "r")
            if fil.mode == 'r':
                lines = fil.read().splitlines()
                first = lines[0].strip().split(" ")
                last = lines[len(lines) - 1].strip().split(" ")
                if (int(first[1]) < dic3["minSize"] or dic3["minSize"] == -1):
                    dic3["minSize"] = int(first[1])
                    dic3["fileName"] = f
                if (int(last[1]) > dic["maxSize"]):
                    dic["maxSize"] = int(last[1])
                    dic["fileName"] = f

                total = 0
                for line in lines:
                    count = line.strip().split(" ")[0]
                    total += int(count)
                if (total > dic2["mostP"]):
                    dic2["mostP"] = total
                    dic2["fileName"] = f
    print(dic) 
    print(dic2)
    print(dic3)
