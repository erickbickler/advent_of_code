import sys
sys.path.append('../')
from utils.old_tree import Tree
from utils.tree import Tree as FullTree

INPUT_FILE_PATH = "inputs/input7.txt"

avalSpace = 70000000
neededSpace = 30000000



class EvalChildren():
    def __init__(self) -> None:
        self.s = 0
        self.spaces = ""
        self.minDirSize = neededSpace
        self.allDirs = []

    def evalChildren(self, node: Tree):
        for i in node.children:
            self.evalChildren(i)
        if node.value == "dir": self.allDirs.append(node)
        
    def calculateChildDir(self, node: Tree):
        total = 0
        self.spaces += "| "
        for i in node.children:
            print(self.spaces, i.name, i.value, i.sum)
            if i.value == "dir":
                self.calculateChildDir(i)
            total += i.sum
        node.sum += total
        self.spaces = self.spaces[:-2]
        

with open(INPUT_FILE_PATH, "r") as input_file:
    base = Tree()
    base.name = "/"
    base.value = "dir"
    currentNode = base
    for line in input_file.read().splitlines():
        line = line.split()
        if line[0] == "$":
            if line[1] == "ls":
                continue
            elif line[1] == "cd" and line[2] == "/":
                node = base
            elif line[1] == "cd" and line[2] != "..":
                childs = [i for i in currentNode.children if i.name == line[2]]
                newCurrentNode = childs[0]
                newCurrentNode.parent = currentNode
                currentNode = newCurrentNode
            elif line[2] == '..':
                currentNode = currentNode.parent
        else:
            if line[0] == "dir":
                newNode = Tree()
                newNode.name = line[1]
                newNode.value = line[0]
                currentNode.children.append(newNode)
            else:
                leaf = Tree()
                leaf.value = "file"
                leaf.sum = int(line[0])
                leaf.name = line[1]
                currentNode.children.append(leaf)
    
    evalch = EvalChildren()
    evalch.calculateChildDir(base)
    minDirSize = neededSpace - (avalSpace - base.sum)
    evalch.minDirSize = minDirSize
    print("minDirSize", minDirSize)
    print()
    evalch.evalChildren(base)
    evalch.allDirs.sort(key=lambda val: val.sum)
    print([i.sum for i in evalch.allDirs if i.sum >= minDirSize][0])

    newBase = FullTree.Node()
    newBase.name = base.name
    newBase.type = base.value
    newBase.data = base.sum
    newBase.children = base.children
    tree = FullTree(newBase)
    tree.print_tree()
