
def main():
    f = open("input.txt", 'r')
    
    path = []
    for line in f:
        depth, layers = map(int,line.split(": "))
        path.append((depth, (layers*2)-2))
    f.close()
    
    count = 0
    total = 1
    while total != 0:
        total = 0
        # print(count)
        for depth,layers in path:
            # print(depth,layers)
            if (depth+count)%layers!=0:
                pass
            else:
                total = 1
                break
        count += 1
        # print("\n\n")
    print(count-1)
main()