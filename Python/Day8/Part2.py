# Day 8 Part 2


def main():
    file = open('./input', 'r')

    line = file.readline().rstrip('\n')

    values = {}
    max_value = 0
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
        if values[split_line[0]] > max_value:
            max_value = values[split_line[0]]
    i = []
    for x in values:
        i.append(values[x])

    print("Max during execution:" + max_value)


main()
