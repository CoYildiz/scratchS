# i believe this is optimized ver
# maybe its not idk


class LinkedList:
    class Node:
        def __init__(self, value, next = None) -> None:
            self.value = value
            self.next = next

        # i saw in stackoverflow that method ------------------------------
        def get(self, index):
            if index >= 0:
                for _ in range(index):
                    self = self.next
                    if not self:
                        break
                return self
        #------------------------------------------------------
    
    # for LinkedList
    def __init__(self, *values) -> None:
        self._head = None
        self._tail = None
        self._length = 0

        for value in values:
            self.append(value)





        
    def __repr__(self) -> str:
       
        if self._length == 0:
            return "[]"
        else:
            last_node = self.Node(-1)
            last_node.next = self._head
            return_string = f"[{last_node.value}"

            while last_node.next:
                last_node = last_node.next
                return_string += f",{last_node.value}"

            return_string += "]"

            return return_string







    def __contains__(self, value) -> bool:

        pass




    def __len__(self) -> int:
        pass

    def __iter__(self) -> None:
        pass


    def append(self, value) -> None:
        
        if self._length == 0:
            new_node = self.Node(value)
            self._head = new_node
            self._tail = new_node
            self._length += 1
        else:
            new_node = self.Node(value)
            self._tail.next = new_node
            self._tail= new_node
            self._length +=1



    def prepend(self, value) -> None:
        new_node = self.Node(value)
        if self._length == 0:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._length += 1


    
    def insert(self, index, value):
        pass



    # if i add a __contains__ func in remove_values i believe is O(n) => O(n^2)
    # so i dont want to add 
    # removing unwanted values from LinkedList (its not check value exist or not)
    def remove_values(self, value) -> None:
        last_node = self._head
        if last_node is not None:
            if last_node.value == value:
                self._head = last_node.next
                self._length -= 1
            else:
                while last_node.next:
                    if last_node.next.value == value:
                        last_node.next = last_node.next.next
                        self._length -= 1
                    last_node = last_node.next
        print(f"Removed {value} value")

    def remove_index(self, index):
        pass


    def pop(self):
        pass

    def get(self, index):
        pass










if __name__ == "__main__":

    ll = LinkedList(1,2)
    ll.remove_values(2)
    
