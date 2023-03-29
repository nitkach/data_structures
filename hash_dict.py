from typing import Any
from list import List


class HashDict:
    ONE_ELEMENT_CAPACITY = 5

    MAX_LOAD_FACTOR = 0.7

    hash = hash

    def __next_capacity(self):
        return int(1.5*len(self.__list))

    def __init__(self):
        self.__list = None
        self.__elem_count = 0

    def __len__(self) -> int:
        return self.__elem_count

    def __iter__(self):
        return self.__list.__iter__()

    def __str__(self) -> str:
        return self.__list.__str__()

    def __eq__(self, other: 'HashDict'):
        if len(self) != len(other):
            return False

        if len(self) + len(other) == 0:
            return True

        index = 0
        while index < len(self.__list):
            if self.__list[index] is not None:
                if other.get(self.__list[index][0]) is None:
                    return False
            index += 1
        return True

    def get(self, key: str) -> Any | None:
        '''
        Get the value by key.
        '''
        if self.__elem_count == 0:
            return None

        bounded_hash = HashDict.hash(key) % len(self.__list)

        while self.__list[bounded_hash] is not None and self.__list[bounded_hash][0] != key:
            bounded_hash = (bounded_hash + 1) % len(self.__list)

        return None if self.__list[bounded_hash] is None else self.__list[bounded_hash][1]

    def set(self, key: str, value: Any) -> Any | None:
        '''
        Set the key-value pair in Hashmap.
        '''
        # list initialization
        if self.__list is None:
            self.__list = List.repeat(HashDict.ONE_ELEMENT_CAPACITY, None)

        # calculate index for the key-value pair by the key using hash function
        # calculated index in the boundaries: [0; len)
        bounded_hash = HashDict.hash(key) % len(self.__list)

        # go through the list until we find an empty space OR matching keys
        while self.__list[bounded_hash] is not None and self.__list[bounded_hash][0] != key:
            bounded_hash = (bounded_hash + 1) % len(self.__list)

        # the keys matched: we write the new value and return the old one
        if self.__list[bounded_hash] is not None and key == self.__list[bounded_hash][0]:
            temp = self.__list[bounded_hash][1]
            self.__list[bounded_hash] = (key, value)
            return temp

        # new key-value pair in list
        self.__list[bounded_hash] = (key, value)
        self.__elem_count += 1

        # check if rehasing is necessary
        if self.__elem_count / len(self.__list) >= HashDict.MAX_LOAD_FACTOR:
            self.__rehash()

    def __rehash(self):
        '''
        temporary save __list
        rewrite __list field
        reset element count to 0
        add elements to the extended list
        '''
        # temporarily saving the list
        temp = self.__list

        # overwriting the __list field with a new list with an increased size
        self.__list = List.repeat(self.__next_capacity(), None)

        # reset the number of elements
        self.__elem_count = 0

        # add elements to the extended list
        for elem in temp:
            if elem is not None:
                self.set(elem[0], elem[1])

    def remove(self, key: str) -> Any:
        '''
        Removes element by the key and return value.
        '''
        if self.__elem_count == 0:
            return None

        for index, elem in enumerate(self.__list):
            if elem is not None and elem[0] == key:
                temp = elem[1]
                self.__list[index] = None
                return temp

        return None

    def from_array(array: 'list') -> 'HashDict':
        h = HashDict()

        for key, value in array:
            h.set(key, value)

        return h
