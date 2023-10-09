from typing import Any


class _Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


class _ListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration

        elem = self.current.elem
        self.current = self.current.next
        return elem


class List:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def __len__(self) -> int:
        '''
        Returns the length of the list.

        # Examples

        >>> from list import List

        >>> l = List()

        >>> assert len(l) == 0

        >>> l.push(1)
        >>> assert len(l) == 1

        >>> l.push(2)
        >>> assert len(l) == 2

        >>> l.push(3)
        >>> assert len(l) == 3
        '''
        return self.__length

    def length(self) -> int:
        '''
        Returns the length of the list.

        # Examples

        >>> from list import List

        >>> l = List()

        >>> assert len(l) == 0

        >>> l.push(1)
        >>> assert len(l) == 1

        >>> l.push(2)
        >>> assert len(l) == 2

        >>> l.push(3)
        >>> assert len(l) == 3
        '''
        return self.__length

    def __eq__(self, other: 'List') -> bool:
        '''
        Comparing two lists.

        If the lists are equal, returns 'True'.
        If the lists are non-equal, returns 'False'.

        # Examples

        >>> from list import List

        >>> l1 = List()
        >>> l2 = List()

        >>> assert l1 == l2
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

        Returns string in format: '[' + list elements separated by ', ' + ']'.
        Empty list returns '[]'.

        # Examples

        from list import List

        l = List()

        assert str(l) == '[]'

        l.push('A')
        l.push('B')

        assert str(l) == '[A, B]'
        '''
        string = '['

        curr_node = self.__head

        while curr_node:
            string += str(curr_node.elem) + ', ' * (curr_node.next is not None)
            curr_node = curr_node.next

        string += ']'

        return string

    # R
    def __getitem__(self, index: int) -> Any:
        '''
        Gets element by index.

        # Exceptions
        Raises exception if 'index >= len'.

        # Examples

        from list import List

        l = List.from_array(['A', 'B'])

        assert l[0] == 'A'
        assert l[1] == 'B'
        '''
        self.__check_index(index)

        count = 0
        for elem in self:
            if count == index:
                return elem
            count += 1

    # U
    def __setitem__(self, index: int, elem: Any) -> None:
        '''
        Sets element by index.

        # Exceptions
        Raises exception if 'index >= len'.

        # Examples

        from list import List

        l = List.from_array(['A', 'B'])

        l[0] = 'B'
        assert l[0] == 'B'

        l[1] = 'A'
        assert l[1] == 'A'
        '''
        self.__check_index(index)

        self.__find_node(index).elem = elem

    def __iter__(self):
        '''
        Returns the iterator of the list
        '''
        return _ListIterator(self.__head)

    def __check_index(self, index, include_border=0) -> None:
        '''
        Checks the entered index in the bounds.

        # Bounds
        - [0; len), include_border = 0:
            Used by all methods that require checking indexes, except insert()
        - [0; len], include_border = 1:
            Used by insert() method

        # Exceptions
        Raises an error if the index is outside the of the borders.

        # Examples

        from list import List

        l = List()

        l.push('X')

        # success
        assert l[0] == 'X'

        # fail
        actual_exception = None

        try:
            l[1] == 'X'
        except Exception as exception:
            actual_exception = exception
        assert "Index 1 is out of bound" in str(actual_exception)
        '''
        if index > self.__length - 1 + include_border or index < 0:
            raise Exception(
                f"Index {index} is out of bound! List length: {self.__length}")

    def __find_node(self, index: int) -> _Node:
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

    def push(self, elem) -> None:
        '''
        Appends a new element to the back of the list.

        # Examples

        from list import List

        l = List()

        l.push('A')
        l.push('B')

        assert l == List.from_array(['A', 'B'])
        '''
        self.insert(self.__length, elem)

    # C

    def insert(self, index: int, elem) -> None:
        '''
        Inserts a new element into the list at the entered index.

        # Exceptions
        Raises exception if 'index > len'.

        # Examples

        from list import List

        l = List()

        l.insert(0, 'A')
        l.insert(1, 'B')

        assert l == List.from_array(['A', 'B'])

        l.insert(0, 'C')

        assert l == List.from_array(['C', 'A', 'B'])
        '''
        self.__check_index(index, 1)

        # empty list
        if self.__head is None:
            self.__head = self.__tail = _Node(elem)
        elif index == 0:
            self.__head = _Node(elem, self.__head)
        elif index == self.__length:
            self.__tail.next = _Node(elem)
            self.__tail = self.__tail.next
        else:
            prev_node = self.__find_node(index - 1)
            prev_node.next = _Node(elem, prev_node.next)

        self.__length += 1
        return

    # D
    def remove(self, index: int) -> Any:
        '''
        Removes the element at entered index and returns it.

        # Exceptions
        Raises excepion if 'index >= len'.

        # Examples

        from list import List

        l = List.from_array(['A', 'B'])

        assert l.remove(0) == 'A' and l == List.from_array(['B'])
        assert l.remove(0) == 'B' and l == List.from_array([])
        '''
        self.__check_index(index)

        if index > 0:
            prev_node = self.__find_node(index - 1)
            elem = prev_node.next.elem

            if index == self.__length - 1:
                self.__tail = prev_node

            prev_node.next = prev_node.next.next
        else:
            elem = self.__head.elem
            self.__head = self.__head.next

        self.__length -= 1
        return elem

    def find(self, elem) -> int | None:
        '''
        Tries to find the entered element in the list and return its index.

        # Examples

        from list import List

        l = List.from_array(['A', 'B', 'C'])

        assert l.find('B') == 1
        assert l.find('D') == None
        '''
        for index, value in enumerate(self):
            if value == elem:
                return index

        return None

    def print(self):
        '''
        Prints list.
        '''
        print(self)

    def from_array(array: list) -> 'List':
        '''
        Creates list from array.

        # Examples

        from list import List

        l1 = List()
        l1.push('A')
        l1.push('B')
        l1.push('C')

        l2 = List.from_array(['A', 'B', 'C'])

        assert l1 == l2
        '''
        list = List()

        for elem in array:
            list.push(elem)

        return list

    def repeat(n_elements: int, inserted_element: Any) -> 'List':
        '''
        Creates a new List: with insterted_element elements,
        and n_elements length.

        # Examples

        from list import List

        l = List.repeat(4, None)

        assert str(l) == "[None, None, None, None]"
        '''
        list = List()

        for _ in range(n_elements):
            list.push(inserted_element)

        return list
