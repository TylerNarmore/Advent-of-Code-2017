#Day 3 Part 1
inValue = 361527
count = 0
y=1
square=1
while y**2 < inValue:
    square = y**2
    print(square, count)
    y += 2
    count +=1

print((square + count), inValue)
print("Answer:", inValue-(square+count)+count)