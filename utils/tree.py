from old_tree import Tree as OldTree 

class Tree:
    class Node:
        def __init__(self):
            self.parent = None
            self.children = []
            self.name = None
            self.type = None
            self.data = 0
        
        def __str__(self) -> str:
            return f"{self.name} {self.type} {self.data}"
    
    def __init__(self, root: Node) -> None:
        self.root = root
        self.__spaces = ""

    def print_tree(self):
        def traverse_nodes(node):
            self.__spaces += "| "
            for child in node.children:
                print(self.__spaces + str(child))
                traverse_nodes(child)
            self.__spaces = self.__spaces[:-2]
        
        print(str(self.root))
        traverse_nodes(self.root)
        self.__spaces = ""