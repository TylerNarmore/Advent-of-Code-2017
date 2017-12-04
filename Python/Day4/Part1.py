#Day4 Part1

file = open('input', 'r')

line = file.readline().rstrip('\n')
lines = []
count = 0
while line != '':
    pw=[]

    splitline = line.split(' ')
    print(splitline)
    for i in splitline:
        x=1
        if(i not in pw):
            pw.append(i)
        else:
            x=0
            break
    count+=x
    line = file.readline().rstrip('\n')
print(count)


