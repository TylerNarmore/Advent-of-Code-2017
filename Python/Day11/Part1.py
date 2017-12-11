# Day 11 Part 1


def main():
    file = open('input', 'r')
    line = file.readline().rstrip('\n')

    split_line = line.split(",")

    y_axis = 0
    x_axis = 0
    z_axis = 0
    for movement in split_line:
        if movement == "ne":
            y_axis += 1
            z_axis -= 1
        elif movement == "se":
            x_axis += 1
            z_axis -= 1
        elif movement == "nw":
            x_axis -= 1
            z_axis += 1
        elif movement == "sw":
            y_axis -= 1
            z_axis += 1
        elif movement == "n":
            y_axis += 1
            x_axis -= 1
        elif movement == "s":
            y_axis -= 1
            x_axis += 1

    print((abs(x_axis)+abs(y_axis)+abs(z_axis))/2)


main()
