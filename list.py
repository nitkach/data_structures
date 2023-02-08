class _Node:
    def __init__(self, elem, next = None):
        self.elem = elem
        self.next = next


class _ListIterator:
    def __init__(self, head):
        self.current = head

    
    def __iter__(self):
        return self


    def __next__(self):
        if self.current == None:
            raise StopIteration

        elem = self.current.elem
        self.current = self.current.next
        return elem


class List:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0


    def __len__(self):
        '''
        Returns the length of the List.
        '''
        return self.__length


    def length(self) -> int:
        '''
        Returns the length of the List.
        '''
        return self.__length


    def __eq__(self, other: 'List'):
        '''
        Comparing two Lists.
        '''
        curr_node = self.__head

        count = 0

        if self.__length != other.length():
            return False

        while count < self.__length:

            if self[count] != other[count]:
                return False

            curr_node = curr_node.next
            count += 1

        return True

    
    def __str__(self) -> str:
        '''
        Creates a string from the List.
        '''
        string = '['

        curr_node = self.__head

        while curr_node:
            string += curr_node.elem + ', ' * (curr_node.next != None) 
            curr_node = curr_node.next 
        
        string += ']'

        return string

    # R
    def __getitem__(self, index):
        '''
        Gets element by index.

        Panics if index >= len.
        '''
        self.__check_index(index)

        count = 0
        for elem in self:
            if count == index:
                return elem
            count += 1

    # U
    def __setitem__(self, index, elem):
        '''
        Sets element by index.

        Panics if index >= len.
        '''
        self.__check_index(index)

        self.__find_node(index).elem = elem
        

    def __iter__(self):
        '''
        Returns the iterator of the List
        '''
        return _ListIterator(self.__head)


    def __check_index(self, index, include_border = 0):
        '''
        Checks the index.

        Panics if index > len, when called by insert() method.
        In other calls panics if index >= len.
        '''

        if index > self.__length - 1 + include_border or index < 0:
            raise Exception(f"Index {index} is out of bound! List length: {self.__length}")

    
    def __find_node(self, index) -> _Node:
        '''
        Finds node by index.
        '''
        curr_node = self.__head

        count = 0

        while count < index:
            curr_node = curr_node.next
            count += 1

        return curr_node


    # C
    def push(self, elem):
        '''
        Appends an element to the tail List.
        '''
        self.insert(self.__length, elem)


    # C
    def insert(self, index, elem):
        '''
        Inserts a new element into the List at the specified index.
        
        Panics if index > len.
        '''
        self.__check_index(index, 1)


        # empty list
        if self.__head == None:
            self.__head = self.__tail = _Node(elem)
            self.__length += 1 # length
            return

        # insert first element
        if index == 0:
            self.__head = _Node(elem, self.__head)
            self.__length += 1 # length
            return

        # insert in tail
        if index == self.__length: # tail
            self.__tail.next = _Node(elem)
            self.__tail = self.__tail.next
            self.__length += 1 # length
            return

        prev_node = self.__find_node(index - 1)
        prev_node.next = _Node(elem, prev_node.next)
        self.__length += 1


    # D
    def remove(self, index):
        '''
        Removes the element at given index and returns it.

        Panics if index >= len.
        '''
        self.__check_index(index)


        if index == 0:
            elem = self.__head.elem
            self.__head = self.__head.next
            self.__length -= 1
            return elem

        prev_node = self.__find_node(index - 1)
        elem = prev_node.next.elem

        if index == self.__length - 1:
            self.__tail = prev_node
        
        prev_node.next = prev_node.next.next
        self.__length -= 1
        
        return elem


    def find(self, elem) -> int | None:
        '''
        Tries to find an element in List and return it's index. 
        '''
        for index, value in enumerate(self):
            if value == elem:
                return index

        return None

    
    def print(self):
        '''
        Prints List.
        '''
        print(str(self))

    
    def from_array(array: list) -> 'List':
        '''
        Creates List from array.
        '''
        l = List()

        for elem in array:
            l.push(elem)

        return l