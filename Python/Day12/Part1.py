# Day 12 Part 1
from Python.Cookbook.Graph import *

def main():
    file = open('input', 'r')
    line = file.readline().rstrip('\n')
    nodes = {}
    while line != '':

        split_line = line.split(" <-> ")

        temp_node = GraphNode(value=int(split_line[0]))
        nodes[int(split_line[0])] = {'node':temp_node,"connections":split_line[1].split(', ')}

        line = file.readline().rstrip('\n')
    graph = Graph([nodes[x]['node'] for x in nodes])

    for node in nodes:
        for connection in nodes[node]['connections']:
            graph.add_edge(nodes[node]['node'],nodes[int(connection)]['node'])

    print(len(graph.dfs_full(nodes[0]['node'])))
main()