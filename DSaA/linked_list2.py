# i believe this is optimized ver


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
        
        pass

    def __contains__(self, value) -> bool:
        pass

    def __len__(self) -> int:
        pass

    def __iter__(self) -> None:
        pass


    def append(self, value) -> None:
        
        if self._length = 0:
            new_node = self.Node(value)
            self_head = new_node
            self._tail = new_node
            self._length += 1
        else:
            new_node = self.Node(value)
            self._tail.next = new_node
            self._tail= new_node
            self._length +=1



    def prepend(self, value) -> None:
        pass
    
    def insert(self, index, value):
        pass

    def remove_value(self, value):
        pass

    def remove_index(self, index):
        pass


    def pop(self, index):
        pass

    def get(self, index):
        pass
