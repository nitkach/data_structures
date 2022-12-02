class Node:
    def __init__(self, next, value):
        self.next = next
        self.value = value


class List:
    def __init__(self):
        self.head = None
        self.tail = None


    def raise_exception_oob(self, index):
        raise Exception(f"Index {index} is out of bound! List length: {self.length()}")

    
    def find_node(self, index):
        '''
        valid indices: [0; list length)
        '''
        if index >= self.length():
            self.raise_exception_oob(index)

        curr_node = self.head

        count = 0

        while count < index:
            curr_node = curr_node.next
            count += 1

        return curr_node


    # C
    def push(self, value):
        new_node = Node(None, value)

        if self.head == None:
            self.head = self.tail = new_node # tail
            return

        curr_node = self.head
        
        while curr_node.next:
            curr_node = curr_node.next
        
        curr_node.next = new_node
        self.tail = new_node # tail


    # C
    def insert(self, index, value):
        if index > self.length() or index < -self.length():
            self.raise_exception_oob(index)

        new_node = Node(None, value)

        # пустой список
        if self.head == None:
            self.head = new_node
            return


        prev_node = self.head


        # вставка на место первого элемента
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return


        count = 0

        prev_node = self.head

        # идём до ноды, предшествующей нужной
        while count < index - 1:
            count += 1
            prev_node = prev_node.next

        # связь новой ноды указывает на 
        new_node.next = prev_node.next 
        prev_node.next = new_node

        
            




    # R
    def get(self, index):
        return self.find_node(index).value


    # U
    def set(self, index, elem):
        self.find_node(index).value = elem

    
    # D
    #def remove(self, index):


    def find(self, value):
        curr_node = self.head

        count = 0

        while curr_node: # проверка на None
            if curr_node.value == value: 
                return count
            count += 1
            curr_node = curr_node.next 

        return None


    def length(self):
        curr_node = self.head

        count = 0

        while curr_node: # проверка на None
            curr_node = curr_node.next 
            count += 1

        return count

    
    def __str__(self) -> str:
        string = '['

        curr_node = self.head

        while curr_node: # проверка на None
            string += curr_node.value + ', ' * (curr_node.next != None) 
            curr_node = curr_node.next 
        
        string += ']'

        return string

    
    def print(self):
        print(str(self))


l = List()

l.push('a')
l.push('b')
l.push('c')
l.print()

l.insert(0, 'd') # написать тест для положит. индексов
l.print()



