import sys
sys.path.append('../')
from utils.old_tree import Tree

INPUT_FILE_PATH = "inputs/input7.txt"

def calculateChildDir(node: Tree):
    total = 0
    for i in node.children:
        if i.value == "dir":
            calculateChildDir(i)
        total += i.sum
    node.sum += total

class EvalChildren():
    def __init__(self) -> None:
        self.s = 0
        self.spaces = ""
    def evalChildren(self, node: Tree):
        self.spaces += "| "
        for i in node.children:
            print(self.spaces, i.name, i.value, i.sum)
            if i.value == "dir" and i.sum <= 100000:
                self.s += i.sum
            self.evalChildren(i)
        self.spaces = self.spaces[:-2]
        

with open(INPUT_FILE_PATH, "r") as input_file:
    base = Tree()
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
    
    calculateChildDir(base)
    evalch = EvalChildren()
    evalch.evalChildren(base)
    print()
    print(evalch.s)
