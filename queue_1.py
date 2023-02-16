from list import List


# FIFO
class Queue:
    def __init__(self):
        self.list = List()   


    def __len__(self):
        '''
        Returns the length of the queue.
        '''
        return self.list.length()


    def length(self):
        '''
        Returns the length of the queue.
        '''
        return self.list.length()


    def __eq__(self, other: 'List'):
        '''
        Comparing two queues.

        If the queues are equal, returns 'True'.
        If the queues are non-equal, returns 'False'.
        '''
        return self.list.__eq__(other)


    def __getitem__(self, index):
        '''
        Gets element by index.

        # Exceptions
        Raises exception if 'index >= len'.
        '''
        return self.list.__getitem__(index)


    def __setitem__(self, index, elem):
        '''
        Sets element by index.

        # Exceptions
        Raises exception if 'index >= len'.
        '''
        self.list.__setitem__(index, elem)


    def __str__(self) -> str:
        '''
        Creates a string from the queue.

        Returns string in format: '[' + queue elements separated by ', ' + ']'.
        Empty queue returns '[]'
        '''
        return str(self.list)


    def __iter__(self):
        '''
        Returns the iterator of the queue.
        '''
        return self.list.__iter__()


    def pop(self):
        '''
        Removes the front element and returns it.

        # Exceptions
        Raises exception if an attempt is made to remove an element from an empty queue.
        '''
        return self.list.remove(0)


    def push(self, elem):
        '''
        Creates a new element at the back of the queue.
        '''
        self.list.push(elem)

    
    def peek(self):
        '''
        Gets the front element.

        # Exceptions
        Raises an exception if an attempt is made to peek into an empty queue.
        '''
        return self.__getitem__(0)

    
    def find(self, elem):
        '''
        Tries to find the entered element in the queue and return its index.
        '''
        return self.list.find(elem)


    def from_array(array: list):
        '''
        Creates queue from array.
        '''
        q = Queue()

        for elem in array:
            q.push(elem)

        return q