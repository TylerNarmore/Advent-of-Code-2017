#Day 2 Part 1

file = open('input', 'r')

lines = []
line = file.readline().rstrip("\n")
sum = 0
while (line != ""):
    line = line.split()
    print (line)
    line = [int(x) for x in line]
    sum += max(line) - min(line)
    line = file.readline().rstrip("\n")

print (sum)