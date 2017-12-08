#Day7 Part2

class Node:
    def __init__(self, name, weight):
        self.name = name
        self.children = []
        self.weight = weight
        self.parent = None
        self.height = None

    def add_child(self, child):
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent

    def get_weight(self):
        sum = self.weight
        #print(self.get_children_weights())
        for i in self.get_children_weights():
            sum+=i
        return sum

    def get_children_weights(self):
        if(len(self.children) != 0):
            children_weights = []
            for child in self.children:
                children_weights.append(child.get_weight())
            return(children_weights)
        else:
            return [0]

    def propagate_height(self, height):
        self.height = height
        for child in self.children:
            child.propagate_height(self.height+1)

    def __str__(self):

        string = "**********************************\n"
        string += "*    Name:  " + self.name + "\n"
        string += "*    Weight:" + str(self.get_weight()) + "\n"
        string += "*    Height:" + str(self.height) + "\n"
        string += "**********************************\n"
        return string

    def __contains__(self, item):
        return item in [x.name for x in self.children]

class Tree:
    def __init__(self):
        self.head = None
        self.height = None

    def set_head(self,head):
        self.head = head


def main():
    file = open('./input', 'r')
    line = file.readline().rstrip("\n")
    tree = Tree()
    nodes = {}
    has_children = {}

    while line != '':
        split_line = line.split()
        name = split_line[0]
        weight = int(split_line[1][1:-1])
        temp_node = Node(name,weight)
        nodes[name] = temp_node
        if len(split_line) > 2:
            has_children[name] = [child_name.rstrip(',') for child_name in split_line[3:]]

        line = file.readline().rstrip("\n")

    for parent_node_name in has_children.keys():
        parent_node = nodes[parent_node_name]
        for child_node_name in has_children[parent_node_name]:
            child_node = nodes[child_node_name]
            child_node.set_parent(parent_node)
            parent_node.add_child(child_node)

    for node in nodes:
        parent = nodes[node].parent

        if(parent == None):
            tree.set_head(nodes[node])
    tree.head.propagate_height(0)

    lowest_node = tree.head
    for key in nodes.keys():
        node = nodes[key]
        children_weights = node.get_children_weights()
        if len(set(children_weights)) != 1:
            if node.height > lowest_node.height:
                lowest_node = node

    values = lowest_node.get_children_weights()
    if values.count(max(set(values))) == 1:
        incorrect_value = max(set(values))
        difference = min(set(values)) - incorrect_value
    else:
        incorrect_value = min(set(values))
        difference = max(set(values)) - incorrect_value

    for child in lowest_node.children:
        if child.get_weight() == incorrect_value:
            print("Incorrect weight found in: " + child.name)
            print("Correct weight is: " + str(child.weight + difference))
            break


main()