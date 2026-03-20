

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None



    def __repr__(self):
        pass

    # O(1) best case - O(n) worst case 
    def __contains__(self, value):
        if self.head = None:
            return False
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False




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

    # O(1) i guess
    def prepend(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            first = Node(value)
            first.next = self.head
            self.head = first

    # O(n) i guess worst case 
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of")
            else:
                last = self.head

                for i in range(index - 1): # i think there is a bug err:"out of range" fix later
                    last = last.next
                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node


    def delete(self, value):
        pass

    def pop(self, index):
        pass

    def get(self, index):
        pass

    def print(self):
        pass

