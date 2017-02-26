class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        print(str(item) + " is pushed")
        self.items.append(item)
        print(stack.items)

    def pop(self):
        print("Pop!")
        self.items.pop()
        print(self.items)

    def peek(self):
        return self.items[len(self.items) -1 ]

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty? : " + "True" if stack.isEmpty() else "False")
    stack.push(1)
    stack.push(5)
    stack.push(2)
    stack.push(4)
    stack.push(3)

    stack.pop()
    stack.pop()
    stack.pop()

    stack.push(4)
