class Tree(object):
    def __init__(self, value):
        self.value = value
        self.leaf_nodes = []
        self.level = 0

    def __str__(self):
        return str(str(self.level) + ': ' + self.value)

    def add(self, tree):
        tree.level = self.level + 1
        self.leaf_nodes.append(tree)

    @staticmethod
    def print_node(root_node):
        print root_node
        for i in root_node.leaf_nodes:
            print i
            Tree.print_node(i)
