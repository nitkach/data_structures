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
        self.length = 0


    def __len__(self):
        return self.length


    def __eq__(self, other: 'List'):
        curr_node = self.head

        count = 0

        if self.length != other.length:
            return False

        while count < self.length:

            if self[count] != other[count]:
                return False

            curr_node = curr_node.next
            count += 1

        return True

    
    def __str__(self) -> str:
        string = '['

        curr_node = self.head

        while curr_node: # проверка на None
            string += curr_node.elem + ', ' * (curr_node.next != None) 
            curr_node = curr_node.next 
        
        string += ']'

        return string


    def __getitem__(self, index):
        self.check_index_borders(index)
        index = self.index_transform(index)

        count = 0
        for elem in self:
            if count == index:
                return elem
            count += 1


    def __setitem__(self, index, elem):
        self.check_index_borders(index)
        self.find_node(self.index_transform(index)).elem = elem
        

    def __iter__(self):
        return ListIterator(self.head)


    def index_transform(self, index: int) -> int:
        '''
        Transform negative indices to correct positive value
        '''
        return index + self.length if index < 0 else index


    def check_index_borders(self, index, border = 1):
        '''
        check index in: 
            [-len; len): border = 1 (default)
            [-len; len]: border = 0
        '''
        if index > self.length - border or index < -self.length:
            self.raise_exception_oob(index)


    def raise_exception_oob(self, index):
        raise Exception(f"Index {index} is out of bound! List length: {self.length}")

    
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
        '''
        self.insert(self.length, elem)


    # C
    def insert(self, index, elem):
        '''
        Insert element in list by moving to right all element standing on the right
        '''
        self.check_index_borders(index, border = 0)

        # empty list
        if self.head == None:
            self.head = self.tail = Node(elem)
            self.length += 1 # length
            return

        index = self.index_transform(index)

        # insert first element
        if index == 0:
            self.head = Node(elem, self.head)
            self.length += 1 # length
            return

        # insert in tail
        if index == self.length: # tail
            self.tail.next = Node(elem)
            self.tail = self.tail.next
            self.length += 1 # length
            return

        prev_node = self.find_node(index - 1)
        prev_node.next = Node(elem, prev_node.next)
        self.length += 1


    # D
    def remove(self, index):
        '''
        Remove element by index
        '''
        if self.check_index_borders(index, border = 1):
            self.raise_exception_oob(index)

        index = self.index_transform(index)

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        prev_node = self.find_node(index - 1)

        if index == self.length - 1:
            self.tail = prev_node
        
        prev_node.next = prev_node.next.next
        self.length -= 1


    def length(self) -> int:
        return self.length


    def find(self, elem) -> int | None:
        '''
        Try to find element in list
        '''
        curr_node = self.head

        count = 0

        while curr_node: # check for None
            if curr_node.elem == elem: 
                return count
            count += 1
            curr_node = curr_node.next 

        return None

    
    def print(self):
        '''
        Print list
        '''
        print(str(self))

    
    def from_array(array):
        '''
        Move element from array to list
        '''
        l = List()

        for elem in array:
            l.push(elem)

        return l


# l = List.from_array(['a', 'b', 'c', 'd'])

# print(l.length)

# print(l)
# print(f"len = {l.length}\n")

# l.insert(-3, 'd')

# print(l)

# for element in l:
#     print(f"element = {element}")

# for i in range(len(l)):
#     print(f"l[{i}] = {l[i]}")

# for i in range(-1, -len(l) - 1, -1):
#     print(f"l[{i}] = {l[i]}")