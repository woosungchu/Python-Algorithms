# simple binary tree
# in this implementation, a node is inserted between an existing node and the root


class BinaryTree():
    """
    Pre-order	      In-order	           Post-order
    Root	          Left sub-tree	       Left sub-tree
    Left sub-tree	  Root	               Right sub-tree
    Right sub-tree	  Right sub-tree	   Root
    """

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left


def readInOrder(tree):
        if tree != None:
            readInOrder(tree.getLeftChild())
            print(tree.getNodeValue())
            readInOrder(tree.getRightChild())



# test tree

if __name__ == "__main__":
    myTree = BinaryTree("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    readInOrder(myTree)
