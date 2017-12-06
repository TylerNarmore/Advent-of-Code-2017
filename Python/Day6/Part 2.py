#Day6 Part2

file = open('./input', 'r')

line = file.readline().rstrip('\n')
banks = [int(x) for x  in line.split('\t')]
previous_states = []
count = 0
newBank = []
temp = False
while banks not in previous_states:
    top = 0
    previous_states.append(list(banks))

    index =0
    for i in banks:
        if i == max(banks):
            break
        index+=1

    top = banks[index]
    banks[index] = 0
    #print(banks)
    for x in range(1,top+1):
       # print((index+x)%len(banks))

        banks[(index+x)%len(banks)]+=1
    count+=1


x=0
for i in previous_states:
    if banks == i:
        break
    x+=1

print(len(previous_states)-x)

