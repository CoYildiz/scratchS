# This linked list is not efficient because it doesn't maintain properties 
# like length or tail in __init__. Using length and tail would make operations faster.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # add cons later maybe lengt and tail for efficient than implement in the funcs
    def __init__(self):
        self.head = None



    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head

            return_string = f"[{last.value}"
            
            while last.next:
                last = last.next
                return_string += f", {last.value}"
            return_string += "]"

            return return_string

    # O(1) best case - O(n) worst case 
    def __contains__(self, value):
        if self.head == None:
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
            while last is not None:
                length += 1
                last = last.next
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

                for _ in range(index - 1):# i think there is a bug err:"out of range" fix later
                    if last is None:
                        raise ValueError("Index out of bounds")
                    last = last.next
                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node

    # O(n) 
    def delete(self, value):
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        last.next = last.next.next
                        return
                    last = last.next

    def pop(self, index = -1):
        if self.head is None:
            raise ValueError("List is emtpy")

        if index == -1:
            if self.head.next is None:
                value = self.head.value
                self.head = None
                return value
            
            prev = None
            current = self.head

            while current.next:
                prev = current
                current = current.next
            
            prev.next = None
            return current.value
        # -----------This part was implemented with help from gpt ---------------
        if index< 0:
            raise ValueError("Index should be >= 0 or use the func like pop()")
        
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            return value

        prev = self.head

        for _ in range(index - 1):
            if prev.next is None:
                raise ValueError("Index out of bounds")

            prev = prev.next
            
        if prev.next is None:
            raise ValueError("Index out of bounds")
            
        value = prev.next.value
        prev.next = prev.next.next
        
        return value
    # ----------------------------------------- 


    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for _ in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            return last.value





if __name__ == "__main__":
    ll = LinkedList()
    ll.append(20)
    ll.append(21)

    print(ll)
