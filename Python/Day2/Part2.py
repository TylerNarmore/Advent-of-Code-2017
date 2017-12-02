#Day 2 Part 2

file = open('input', 'r')

lines = []
line = file.readline().rstrip("\n")
sum = 0
while (line != ""):
    flag = 0
    line = line.split()
    print (line)
    line = [int(x) for x in line]
    for i in line:
        for j in line:
            if (j%i == 0 and j / i != 1):
                sum += j/i
                flag = 1

    line = file.readline().rstrip("\n")
print (sum)