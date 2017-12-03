#Day 3 Part 2
inValue = 361527
#Pulled from https://oeis.org/A141481
SquareSpiralNumbersLocation = 'b141481.txt'
file = open(SquareSpiralNumbersLocation, 'r')
number = 0
while number < inValue:
    line = file.readline()

    number = int(line.split(' ')[1])

print(number)