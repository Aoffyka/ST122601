class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.p = None 

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)
                #Minimum

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)
    # add val 
    def _treeMinimum(self,val):
        node = self.find(val)
        if self.root is not None:
            return self.treeMinimum(node)
        else:
            return None 

    # Pseudocode from the slide
    def treeMinimum(self,node):
        while node.l is not None:
            node = node.l
        return node
    # add val
    def _treeSuccessor(self,val):
        node = self.find(val)
        if self.root is not None:
            return self.treeSuccessor(node)
    
    # Pseudocode from the slide
    def treeSuccessor(self,node):
        if node is None:
            return None 
        if node.r is not None:
            return self._treeMinimum(node.r.v)
        y = node.p
        while y is not None and node == y.r:
            node = y
            y = y.p 
        return y


tree = Tree()
tree.add(12)
tree.add(8)
tree.add(9)
tree.add(13)
tree.add(1)
tree.add(5)

tree.printTree()
#print(tree.find(3).v)
#print(tree.find(10))
#tree.deleteTree()
#tree.printTree()



success = input('Select Tree successor: ')
successor = tree._treeSuccessor(int(success))
if successor is None:
    print("No child")
else:
    print(successor.v)



