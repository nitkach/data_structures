from typing import Any
from list import List


class SortedListDict:
    def __init__(self):
        self.__list = List()

    def __eq__(self, other):
        self.__list.__eq__(other)

    def __str__(self) -> str:
        return self.__list.__str__()

    def __len__(self) -> int:
        return self.__list.length()

    def __find_gte_or_length(self, key: str) -> int:
        '''
        gte means greater or equal
        '''
        # binary search

        left = 0  # left border
        right = len(self.__list) - 1  # right border
        middle = 0

        while left <= right:
            middle = (left + right)//2

            if self.__list[middle][0] == key:
                return middle
            elif key > self.__list[middle][0]:
                left += 1
            else:
                right -= 1

        # check if List is empty to avoid exception
        return middle if len(self.__list) == 0 or key < self.__list[middle][0] else middle + 1

    def get(self, key: str) -> Any | None:
        '''
        Gets value in the tuple by searching by the key
        '''
        index = self.__find_gte_or_length(key)

        if index == self.__list.length():
            return None

        return self.__list[index][1]

    def set(self, key: str, value: Any) -> Any | None:
        '''
        Inserts a new element into a sorted list.
        '''
        index = self.__find_gte_or_length(key)

        if index == self.__list.length() or key != self.__list[index][0]:
            self.__list.insert(index, (key, value))
            return None

        temp = self.__list[index][1]
        self.__list[index] = (key, value)
        return temp

    def remove(self, key: str) -> Any:
        '''
        Removes the element by the key and returns value.
        '''
        if self.__list.length() == 0:
            return None

        index = self.__find_gte_or_length(key)

        if index != self.__list.length() and self.__list[index][0] == key:
            return self.__list.remove(index)[1]

        return None

    def from_array(array):
        '''
        Creates a sorted list from array.
        '''
        d = SortedListDict()

        for key, value in array:
            d.set(key, value)

        return d
