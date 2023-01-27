from list import List


class QueueIterator:
    def __init__(self, head) -> None:
        self.current = head

    
    def __iter__(self):
        return self


    def __next__(self):
        if self.current == None:
            raise StopIteration

        elem = self.current.elem
        self.current = self.current.next
        return elem


# FIFO
class Queue:
    def __init__(self):
        self.list = List()   


    def __len__(self):
        return self.list.length()


    def length(self):
        return self.list.length()


    def __eq__(self, other: 'List'):
        return self.list.__eq__(other)


    def __getitem__(self, index):
        return self.list.__getitem__(index)


    def __setitem__(self, index, elem):
        self.list.__setitem__(index, elem)


    def __str__(self) -> str:
        return str(self.list)


    def __iter__(self):
        return QueueIterator(self.list.head)


    def pop(self):
        return self.list.remove(0)


    def push(self, elem):
        self.list.push(elem)

    
    def peek(self):
        return self.__getitem__(0)

    
    def find(self, elem):
        return self.list.find(elem)


    def from_array(array: list):
        q = Queue()

        for elem in array:
            q.push(elem)

        return q