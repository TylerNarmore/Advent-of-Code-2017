#Day 1 Part 1

file = open('input', 'r')

lines = []
line = file.readline().rstrip("\n")
sum = 0
for i in range(1,len(line)):
    if line[i-1] == line[i]:
        sum+=int(line[i-1])
if(line[0] == line[-1]):
        sum += int(line[0])
print(sum)
