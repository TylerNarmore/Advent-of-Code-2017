

def main():
    dancers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

    f=open("Day16/Input.txt", 'r')
    instructions = f.read().split(',')
    f.close()
    for instruction in instructions:
        move = instruction[0]
        
        #spin
        if move == 's':
            dancers = dancers[-int(instruction[1:]):] +dancers[:-int(instruction[1:])] 
        #Exchange
        elif(move == 'x'):
            dancer1,dancer2 = map(int, instruction[1:].split('/'))
            temp = dancers[dancer1]
            dancers[dancer1] = dancers[dancer2]
            dancers[dancer2] = temp
        #Partner
        elif(move == 'p'):
            dancer1,dancer2 = instruction[1:].split('/')
            dancer1_loc = dancers.index(dancer1)
            dancer2_loc = dancers.index(dancer2)
            dancers[dancer1_loc] = dancer2
            dancers[dancer2_loc] = dancer1
        
    print(''.join(dancers))
    
main()