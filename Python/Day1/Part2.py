#Day 1 Part 2

file = open('input', 'r')

lines = []
line = file.readline().rstrip("\n")
sum = 0
lengthdiv2 = len(line)/2
for i in range(len(line)):
    print((i+lengthdiv2) % len(line))
    if line[i] == line[int((i+lengthdiv2) % len(line))]:
        sum+=int(line[i])
print(sum)
