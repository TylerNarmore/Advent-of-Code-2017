# Day 8 Part 1


def main():
    file = open('./input', 'r')

    line = file.readline().rstrip('\n')

    values = {}
    while line != '':

        split_line = line.split()
        if split_line[0] not in values.keys():
            values[split_line[0]] = 0
        if split_line[4] not in values.keys():
            values[split_line[4]] = 0

        condition = "values[split_line[4]]" + split_line[5] + " " + split_line[6]

        if eval(condition):
            if split_line[1] == "inc":
                values[split_line[0]] += int(split_line[2])
            else:
                values[split_line[0]] -= int(split_line[2])
        line = file.readline().rstrip('\n')

    i = []
    for x in values:
        i.append(values[x])

    print("Max at end of Execution:", max(i))


main()
