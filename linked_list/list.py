class Node:
    def __init__(self, next, value):
        self.next = next
        self.value = value


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def raise_exception_oob(self, index):
        raise Exception(f"Index {index} is out of bound! List length: {self.length}")

    
    def find_node(self, index):
        '''
        valid indices: [0; list length)
        '''
        if index >= self.length:
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
            self.length += 1 # length
            return

        curr_node = self.head
        
        while curr_node.next:
            curr_node = curr_node.next
        
        curr_node.next = new_node
        self.tail = curr_node.next # tail
        self.length += 1 # length


    # C
    def insert(self, index, value):
        if index > self.length or index < -self.length:
            self.raise_exception_oob(index)

        new_node = Node(None, value)

        # пустой список
        if self.head == None:
            self.head = self.tail = new_node
            self.length += 1 # length
            return


        # вставка на место первого элемента
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1 # length
            return

        # вставка в конец списка
        if index == self.length: # tail
            self.tail.next = new_node
            self.tail = self.tail.next
            self.length += 1 # length
            return


        prev_node = self.head

        count = 0

        prev_node = self.head

        # идём до ноды, предшествующей нужной
        while count < index - 1:
            count += 1
            prev_node = prev_node.next

        # связь новой ноды указывает на 
        new_node.next = prev_node.next 
        prev_node.next = new_node
        self.length += 1


    # R
    def get(self, index):
        return self.find_node(index).value


    # U
    def set(self, index, elem):
        self.find_node(index).value = elem

    
    # D
    def remove(self, index):
        if index >= self.length or index < -self.length:
            self.raise_exception_oob(index)

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        curr_node = self.head

        count = 0

        while count < index - 1:
            curr_node = curr_node.next
            count += 1

        if index == self.length - 1:
            self.tail = curr_node
        
        curr_node.next = curr_node.next.next
        self.length -= 1


    def find(self, value):
        curr_node = self.head

        count = 0

        while curr_node: # проверка на None
            if curr_node.value == value: 
                return count
            count += 1
            curr_node = curr_node.next 

        return None


    # def length(self):
    #     curr_node = self.head

    #     count = 0

    #     while curr_node: # проверка на None
    #         curr_node = curr_node.next 
    #         count += 1

    #     return count


    def __eq__(self, other: 'List'):
        curr_node = self.head

        count = 0

        if self.length != other.length:
            return False

        while count < self.length:

            if self.get(count) != other.get(count):
                return False

            curr_node = curr_node.next
            count += 1

        return True

    
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


def test_equals_success():
    L1 = List()
    L2 = List()

    L1.push('p')
    L1.push('o')
    L1.push('n')

    L2.push('p')
    L2.push('o')
    L2.push('n')

    assert L1 == L2, f"{L1} == {L2}."


def test_equals_fail():
    L1 = List()
    L2 = List()

    L1.push('p')
    L1.push('o')
    L1.push('n')

    L2.push('n')
    L2.push('o')
    L2.push('p')


    assert L1 != L2, f"{L1} != {L2}."


def test_insert_():
    L1 = List()
    L2 = List()
    



l = List()

l.push('a')
l.push('b')
l.push('c')

print('\n')
l.print()
print(f"len = {l.length}, tail.value = {l.tail.value}\n")

l.insert(3, 'd') # написать тест для положит. индексов
l.print()
print(f"len = {l.length}, tail.value = {l.tail.value}\n")

l.remove(3)
l.print()
print(f"len = {l.length}, tail.value = {l.tail.value}\n")


test_equals_success()
test_equals_fail()