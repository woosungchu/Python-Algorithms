class Queue:
"""
    First In First Out
"""
    def __init__(self):
        self.items = []

    def add(self,item):
        self.items.append(item)

    def delete(self):
        itemToDelete = self.items[0];
        del self.items[0]
        return itemToDelete

    def size(self):
        return len(self.items)

    def report(self):
        return self.items

if __name__ == "__main__":
    myQueue = Queue()
    myQueue.add("Bob")
    myQueue.add("Terry")
    myQueue.add("James")
    myQueue.add("Jamie")
    myQueue.add("Carrie")
    myQueue.add("Brodie")
    myQueue.add("Tanya")

    print(myQueue.size())
    print(myQueue.report())
    print(myQueue.delete())
    print(myQueue.report())
