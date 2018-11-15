import sys
import random

# split up [n] job size into [m] machines
def assign(n, m):
    groups = []
    # setup the groups with 1 each [1,1,1...,1]
    for i in range(0,m):
        groups.append(1)
    n -= m
    # randomly choose an index to fill by one
    while n > 0:
        index = random.randint(0,m-1)
        groups[index] += 1
        n -= 1
    # make the string from list
    line = ""
    for g in groups:
        line += str(g) + " "
    return line + " \n"

# Handle command args
if (len(sys.argv) < 2):
    print("missing args")
    sys.exit()
if (len(sys.argv) > 2):
    machines = sys.argv[2]
    filename = sys.argv[1]
else:
    filename = sys.argv[1]
    machines = 5

print("Reading from file: " + filename)
print("Using [" + str(machines) + "] machines")

# read file 
file = open(filename, "r")
output = open("output_"+filename, "w")
# process and output to file
for line in file:
    try:
        workload = int(line)
        value = assign(workload, int(machines))
        output.write(value)
    except ValueError as err:
        print(err)
        workload = ""
