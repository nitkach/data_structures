from list import List


# FIFO
class Queue:
    def __init__(self):
        self.list = List()   


    def __len__(self):
        '''
        Returns the length of the Queue.
        '''
        return self.list.length()


    def length(self):
        '''
        Returns the length of the Queue.
        '''
        return self.list.length()


    def __eq__(self, other: 'List'):
        '''
        Comparing two Queues.
        '''
        return self.list.__eq__(other)


    def __getitem__(self, index):
        '''
        Gets element by index.

        Panics if index >= len.
        '''
        return self.list.__getitem__(index)


    def __setitem__(self, index, elem):
        '''
        Sets element by index.

        Panics if index >= len.
        '''
        self.list.__setitem__(index, elem)


    def __str__(self) -> str:
        '''
        Creates a string from the Queue.
        '''
        return str(self.list)


    def __iter__(self):
        '''
        Returns the iterator of the Queue.
        '''
        return self.list.__iter__()


    def pop(self):
        '''
        Removes the front element and returns it.

        Panics if len == 0 (Queue is empty).
        '''
        return self.list.remove(0)


    def push(self, elem):
        '''
        Creates a new element at the back of the Queue.
        '''
        self.list.push(elem)

    
    def peek(self):
        '''
        Gets the front element.

        Panics if len == 0 (Queue is empty).
        '''
        return self.__getitem__(0)

    
    def find(self, elem):
        '''
        Tries to find an element in the Queue and returns it.
        '''
        return self.list.find(elem)


    def from_array(array: list):
        '''
        Creates Queue from array.
        '''
        q = Queue()

        for elem in array:
            q.push(elem)

        return q