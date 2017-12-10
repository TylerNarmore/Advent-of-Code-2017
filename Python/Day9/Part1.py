# Day 9 Part 1
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
    test = re.split(pattern, cleaned_data)

    removed_trash = "".join(test)
    print(removed_trash)

    toral_score = 0
    x = 0
    for i in removed_trash:
        if i == "{":
            x += 1
        elif i == "}":
            toral_score += x
            x -= 1

    print(toral_score)


main()
