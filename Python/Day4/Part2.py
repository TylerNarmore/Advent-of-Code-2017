#Day4 Part2

file = open('input', 'r')

line = file.readline().rstrip('\n')
lines = []
count = 0
while line != '':
    pw=[]
    splitline = line.split(' ')

    for i in splitline:
        x=1
        i = set(i)

        if(i not in [set(y) for y in pw]):
            pw.append(i)
        else:
            x=0
            break
    count+=x
    line = file.readline().rstrip('\n')
print(count)
