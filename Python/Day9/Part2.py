# Day 9 Part 2
import re


def main():

    file = open('./input', 'r')

    data = file.read().rstrip('\n')

    cleaned_data = []
    i = 0
    while i < len(data):
        cur_char = data[i]
        if cur_char == "!":
            i += 2
        else:
            cleaned_data.append(data[i])
            i += 1

    cleaned_data = "".join(cleaned_data)

    pattern = "\<[^>]*\>"
    test = re.findall(pattern, cleaned_data)

    num_trash = len(test) * 2

    joined = ''.join(test)

    print(len(joined)-num_trash)


main()
