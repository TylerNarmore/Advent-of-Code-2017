# Day 10 Part 2


def main():
    file = open('input', 'r')
    input_data = file.read().rstrip('\n')
    data = [ord(x) for x in input_data]
    data.append(17)
    data.append(31)
    data.append(73)
    data.append(47)
    data.append(23)
    base_list = list(range(256))

    skip_size = 0
    start_spot = 0
    for i in range(64):
        for length in data:
            working_list = []
            for index in range(length):
                working_list.append(base_list[(start_spot + index) % 256])
            reversed_list = list(reversed(working_list))

            for reversed_item in range(len(reversed_list)):
                base_list[(start_spot + reversed_item) % 256] = reversed_list[reversed_item]
            start_spot += (length + skip_size) % 256
            skip_size += 1

    dense_hash = []
    sparse_hash_loc = 0
    for i in range(16):
        running_xor = base_list[sparse_hash_loc]
        for x in range(1, 16):
            running_xor = running_xor ^ base_list[sparse_hash_loc+x]
        dense_hash.append("{0:#0{1}x}".format(running_xor, 4))
        sparse_hash_loc += 16

    formatted_dense_hash = [str(x)[2:] for x in dense_hash]
    formatted_dense_hash = ''.join(formatted_dense_hash)

    print(formatted_dense_hash)


main()
