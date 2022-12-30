class Node:
    def __init__(self, elem, next = None):
        self.elem = elem
        self.next = next


class ListIterator:
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
        self.head = None
        self.tail = None
        self._length = 0


    def __len__(self):
        return self._length


    def length(self) -> int:
        return self._length


    def __eq__(self, other: 'List'):
        '''
        pre: 
            two lists
        post: 
            True if lists are equals, False if not
        '''
        curr_node = self.head

        count = 0

        if self._length != other.length():
            return False

        while count < self._length:

            if self[count] != other[count]:
                return False

            curr_node = curr_node.next
            count += 1

        return True

    
    def __str__(self) -> str:
        '''
        pre: 
            any list
        post: 
            returns list as string 
        '''
        string = '['

        curr_node = self.head

        while curr_node: # проверка на None
            string += curr_node.elem + ', ' * (curr_node.next != None) 
            curr_node = curr_node.next 
        
        string += ']'

        return string

    # R
    def __getitem__(self, index):
        '''
        Get element by index

        pre: 
            index in:
                [-len; len)
        ? inv: 
            index validation 
        post: 
            returns element by index
        '''
        index = self.check_index_and_transform(index)

        count = 0
        for elem in self:
            if count == index:
                return elem
            count += 1

    # U
    def __setitem__(self, index, elem):
        '''
        Set element by index

        pre: 
            index in:
                [-len; len)
            elem:
                any
        ? inv: 
            index validation
        post: 
            sets element by index
        '''
        index = self.check_index_and_transform(index)
        self.find_node(index).elem = elem
        

    def __iter__(self):
        return ListIterator(self.head)


    def check_index_and_transform(self, index, include_border = 0):
        '''
        Check index. If correct, returns new index value.

        pre:
            index must be in:
                [-len; len) if include_border = 0, default.
                [-len; len] if include_border = 1, for List.push and Queue.put;
        post: 
            returns transformed index
        '''

        if index > self._length + include_border or index < -self._length:
            raise Exception(f"Index {index} is out of bound! List length: {self._length}")

        return index + self._length if index < 0 else index

    
    def find_node(self, index) -> Node:
        '''
        Find node by index
        '''
        curr_node = self.head

        count = 0

        while count < index:
            curr_node = curr_node.next
            count += 1

        return curr_node


    # C
    def push(self, elem):
        '''
        Add element to tail list

        pre:
            elem:
                any
        post: 
            element is added to the end of the list
        '''
        self.insert(self._length, elem, 1)


    # C
    def insert(self, index, elem, include_border = 0):
        '''
        Insert element in list by moving to right all element standing on the right
        
        pre:
            index in:
                [-len; len) if include_border = 0, default.
                [-len; len] if include_border = 1, for List.push and Queue.put;
            elem:
                any
        post:
            element is inserted at index
        '''
        index = self.check_index_and_transform(index, include_border)


        # empty list
        if self.head == None:
            self.head = self.tail = Node(elem)
            self._length += 1 # length
            return

        # insert first element
        if index == 0:
            self.head = Node(elem, self.head)
            self._length += 1 # length
            return

        # insert in tail
        if index == self._length: # tail
            self.tail.next = Node(elem)
            self.tail = self.tail.next
            self._length += 1 # length
            return

        prev_node = self.find_node(index - 1)
        prev_node.next = Node(elem, prev_node.next)
        self._length += 1


    # D
    def remove(self, index):
        '''
        Remove element by index

        pre:
            index in:
                [-len; len)
        post:
            element is removed by index
        '''
        index = self.check_index_and_transform(index)


        if index == 0:
            self.head = self.head.next
            self._length -= 1
            return

        prev_node = self.find_node(index - 1)

        if index == self._length - 1:
            self.tail = prev_node
        
        prev_node.next = prev_node.next.next
        self._length -= 1


    def find(self, elem) -> int | None:
        '''
        Try to find element in list

        pre:
            elem:
                any
        post:
            returns the index of the element if it contained in the List, otherwise returns None
        '''
        for index, value in enumerate(self):
            if value == elem:
                return index

        return None

    
    def print(self):
        '''
        Print list
        '''
        print(str(self))

    
    def from_array(array: list) -> 'List':
        '''
        Move element from array to list
        '''
        l = List()

        for elem in array:
            l.push(elem)

        return l