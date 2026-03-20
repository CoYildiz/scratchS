

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None



    def __repr__(self):
        pass

    
    def __contains__(self):
        pass
    # O(n)
    def __len__(self):
        if self.head == None:
            return 0
        else:
            length = 0
            last = self.head
            while last.next:
                length += 1
            return length
    # O(n) 
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = Node(value)

    def prepend(self, value):
        pass

    def insert(self, value, index):
        pass

    def delete(self, value):
        pass

    def pop(self, index):
        pass

    def get(self, index):
        pass

    def print(self):
        pass


