from list import Node, List, ListIterator


class Queue(List):
    def __init__(self):
        self.head = None
        self.length = 0


    def __getitem__(self, index):
        self.check_index_borders(index)
        if index != 0:
            raise Exception(f"You cannot access to this element!")
        return self.head.elem


    def __setitem__(self, index, elem):
        self.check_index_borders(index)
        raise Exception(f"You cannot change value!")


    def put(self, elem):
        if self.head == None:
            self.head = Node(elem)
            self.length += 1
            return

        curr_node = self.find_node(self.length - 1)
        curr_node.next = Node(elem)
        self.length += 1
    # put == push
    
    # pop == remove(0)
    def pop(self):
        if self.head == None:
            raise Exception(f"Queue is empty! Nothing to pop.")

        pop = self.head.elem

        self.head = self.head.next

        return pop


q = Queue()

q.put('a')
q.put('b')
q.put('c')

q.pop()

for elem in q:
    print(elem)