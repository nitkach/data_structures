class Node:
    def __init__(self, next, elem):
        self.next = next
        self.elem = elem


class List:
    def __init__(self): # C
        self.head = None

    def insert(self, elem): # C
        new_elem = Node(None, elem)
        if self.head is None:
            self.head = Node(None, elem)
            return
        
        last_elem = self.head
        while last_elem.next:
            last_elem = last_elem.next
        last_elem = new_elem
        print(self.head.elem)


    def remove(self, index): # D
        pass


    def set(self, index, elem): # U
        pass


    def get(self, index): # R
        # last_elem = self.head

    #     node_index = 0

    #     while node_index <= index:
        
        # if index > self.length() - 1:
            # raise Exception(f"Index {index} is out of bound! Length: {self.length()}")

        node = self.head

        i = 0

        while i < index:
            node = node.next
            i += 1

        return node.elem


    def length(self): # R
        node = self.head

        if self.head == None:
            return 0

        count = 1

        while node.next != None:
            count += 1
            node = node.next
        
        return count

    
    def print(self): # вывод списка в консоль
        pass

    
    def find(self, elem): # -> index | None 
        pass


l = List()

l.insert('a')
l.insert('b')
# l.insert_3('c')

print(l.get(0))
print(l.get(1))

# def insert_1(self, elem):
#     self.head = Node(None, elem)
#     print(self.head.elem)

# def insert_2(self, elem):
#     self.head.next = Node(None, elem)
#     print(self.head.elem)

# def insert_3(self, elem):
#     self.head.next.next = Node(None, elem)


# index = 0
# elem = 1

# self.head = Node(next = None, elem = ...)
# node = self.head(next = None, elen = ...)
# 
# count = 0
# while node.next != None:
#   count += 1
#   node = node.next 
# --
# count = 1
# while None.next != None:
#   

# index = 2
# self.head = Node(next = None)
# node = Node(next = None)
# i = 0
# while 0 < 2:
#   node = Node(next = None).next = self.head.next = None
#   i = 1
# --
#   node = None.next
#   node = 

# ... is None; ... == None
# https://pythonworld.ru/tipy-dannyx-v-python/none.html