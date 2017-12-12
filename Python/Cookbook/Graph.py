class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = set()

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return self.value


class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def add_node(self, val):
        new_node = GraphNode(val)
        if new_node not in self.nodes:
            self.nodes.append(new_node)
        return(new_node)

    def add_edge(self, node1, node2):
        if node2 not in node1.edges:
            node1.edges.add(node2)
        if node1 not in node2.edges:
            node2.edges.add(node1)

    def bfs(self, start, goal=None):
        visited = []
        queue = [[start]]
        if(start == goal):
            return []

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in visited:
                for edge in node.edges:
                    new_path = list(path)
                    new_path.append(edge)
                    queue.append(new_path)
                    if edge == goal:
                        return new_path
                visited.append(node)
        return "Not connected"

    def dfs_full(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                #print(vertex.edges)
               # print(visited)
                stack.extend(vertex.edges - visited)
        return visited

    def dfs(self, start, goal, path=None):
        if path is None:
            path = [start]
        if start == goal:
            yield path
        for next in start.edges - set(path):
            yield from self.dfs(next, goal, path + [next])
