class TreeNode:
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
        self.head.propagate_height(0)

