# Day 10 Part 1


def main():
    file = open('input', 'r')

    data = [int(x) for x in file.read().rstrip('\n').split(',')]

    base_list = list(range(256))

    skip_size = 0
    start_spot = 0
    for length in data:
        working_list = []
        for i in range(length):
            working_list.append(base_list[(start_spot+i) % 256])
        reversed_list = list(reversed(working_list))

        for i in range(len(reversed_list)):
            base_list[(start_spot+i) % 256] = reversed_list[i]
        start_spot += (length + skip_size) % 256
        skip_size += 1

    print(base_list[0]*base_list[1])


main()
