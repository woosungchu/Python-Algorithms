class Node:
    def __init__(self,contents=None,next=None):
        self.contents = contents
        self.next = next

    def getContents(self):
        return self.contents

    def __str__(self):
        return str(self.contents)

def print_list(node):
    while node:
        print(node.getContents())
        node = node.next
    print()

if __name__ == "__main__":
    node1 = Node("car")
    node2 = Node("bus")
    node3 = Node("plane")

    node1.next = node2
    node2.next = node3

    print_list(node1)
