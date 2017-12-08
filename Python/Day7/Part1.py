#Day7 Part1

file = open('./input', 'r')

line = file.readline().rstrip('\n')
lines = []
count = 0
bottom_leaf = []
branch = {}
while line != '':
    splitline =line.split()
    if len(splitline) == 2:
        bottom_leaf.append(splitline[0])
    else:
        branch[splitline[0]]=[x.rstrip(',') for x in splitline[3:]]
    line = file.readline().rstrip('\n')

def find_leafs(folder, height):
    max_height = height
    if(folder in bottom_leaf):
        return height
    else:
        for item in branch[folder]:
            newHeight = find_leafs(item, height+1)
            if(newHeight > max_height):
                max_height = newHeight

        return(max_height)
maximum = 0
for i in branch.keys():
    height = find_leafs(i, 0)
    if height > maximum:
        bottom_folder = i
        maximum = height

print(bottom_folder)

