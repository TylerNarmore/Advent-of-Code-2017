def knotHash(input_data):
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

    return formatted_dense_hash

def bfs(graph, loc_x, loc_y):
    graph[loc_y][loc_x] = "."
    #Check up
    if loc_y > 0:
        if graph[loc_y-1][loc_x] == "#":
            graph = bfs(graph, loc_x, loc_y-1)
    #Check Right
    if loc_x < 127:
        if graph[loc_y][loc_x+1]== "#":
            graph = bfs(graph, loc_x+1, loc_y)
    #Check Down
    if loc_y < 127:
        if graph[loc_y+1][loc_x]== "#":
            graph = bfs(graph, loc_x, loc_y+1)
    #Check Left
    if loc_x > 0:
        if graph[loc_y][loc_x-1]== "#":
            graph = bfs(graph, loc_x-1, loc_y)

    return graph

def main():
    disk = []
    
    #create graph
    for i in range(128):
        hash_seq = knotHash("uugsqrei-"+str(i))
        row = list(bin(int(hash_seq, 16))[2:].zfill(128).replace('1',"#").replace("0","."))
        disk.append(row)
    
    print("Finding Segments")
    #Search Graph
    segments = 0
    for y in range(128):
        for x in range(128):
            if (disk[y][x] == "#"):
                disk = bfs(disk, x, y)
                segments+=1
    print("Total number of segments:",segments)
main()