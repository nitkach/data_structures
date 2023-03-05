from typing import Any
from list import List


class SortedListDict:
    def __init__(self):
        self.__list = List()

    def __eq__(self, other):
        self.__list.__eq__(other)

    def __str__(self) -> str:
        return self.__list.__str__()

    def __find_gte_or_length(self, key: str) -> int:
        '''
        gte means greater or equal
        '''
        # TODO: binary search

        index = 0

        while index < self.__list.length() and self.__list[index][0] < key:
            index += 1

        return index

    def get(self, key: str) -> Any | None:
        index = self.__find_gte_or_length(key)

        if index == self.__list.length():
            return None

        return self.__list[index][1]

    def set(self, key: str, value: Any) -> Any | None:
        index = self.__find_gte_or_length(key)

        if index == self.__list.length() or key != self.__list[index][0]:
            self.__list.insert(index, (key, value))
            return None

        temp = self.__list[index][1]
        self.__list[index] = (key, value)
        return temp

    def remove(self, key: str) -> Any:
        index = self.__list.find(key)

        if index is not None:
            return self.__list.remove(index)[1]

        return index

    def from_array(array):
        d = SortedListDict()

        for key, value in array:
            d.set(key, value)

        return d
