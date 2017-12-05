#Day5 Part1

file = open('./input', 'r')

line = file.readline().rstrip('\n')
lines = []
count = 0
while line != '':
    lines.append(int(line))
    line = file.readline().rstrip('\n')

i=0
while i <= len(lines):
    count+=1
    x=i
    i+=lines[i]
    lines[x] +=1
    if(i >= len(lines)):
        break

print(count)
