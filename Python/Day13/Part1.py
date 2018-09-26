

def main():
    f = open("input.txt", 'r')
    total = 0
    for line in f:
        depth, layers = map(int,line.split(": "))
        if (depth % ((layers*2)-2)) == 0:
            total += depth*layers
    f.close()
    print(total)

main()