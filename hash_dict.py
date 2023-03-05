from typing import Any
from list import List


class HashDict:
    ONE_ELEMENT_CAPACITY = 5

    MAX_LOAD_FACTOR = 0.7

    hash = hash


    def next_capacity(self):
        return int(1.5*len(self.__list))


    def __init__(self):
        self.__list = None
        self.__elem_count = 0


    def __eq__(self, other):
        pass


    def __str__(self) -> str:
        return self.__list.__str__()


    def get(self, key: str) -> Any | None:
        pass


    def set(self, key: str, value: Any) -> Any | None:
        # empty cell: None
        # 
        # insert into empty cell | maybe rehash
        # [_, _, _, _, _] 6
        # [_, 6(1), _, _, _] 6 % 5 = 1
        # 
        #
        # insert into occupied cell (not cycled) | maybe rehash
        # [_, 1(1), _, _, _] 6 % 5 = 1
        # [_, 1(1), 6(1), _, _]
        #
        #
        # [_, 1(1), 6(1, b), _, _] 6 % 5 = 1 | no rehash
        # [_, 1(1), 6(1, a), _, _]
        #
        #
        # insert into occupied cell (cycled) | maybe rehash
        # [_, _, _, _, 4(4)] 9 % 5 = 4
        # [9(4), _, _, _, 4(4)]
        #
        #
        # [_, _, _, _, 4(4, a)] 4 % 5 = 4, b | no rehash
        # [_, _, _, _, 4(4, b)]
        #
        #
        # [1(1), 2(2), 3(3), 4(4), 5(5), _, _] 6
        # rehash: create copy, with next capacity.
        # then, recursive call set
        # [1(1), 2(2), 3(3), 4(4), 5(5), 6(6), _] 
        # [1(1), 2(2), 3(3), 4(4), 5(5), 6(6), _, _, _]
        if self.__list is None:
            self.__list = List.repeat(HashDict.ONE_ELEMENT_CAPACITY, None)

        bounded_hash = HashDict.hash(key) % len(self.__list)

        while self.__list[bounded_hash] != None and self.__list[bounded_hash][0] != key:
            bounded_hash = (bounded_hash + 1) % len(self.__list)

        if self.__list[bounded_hash] != None and key == self.__list[bounded_hash][0]:
            temp = self.__list[bounded_hash][1]
            self.__list[bounded_hash] = (key, value)
            return temp

        self.__list[bounded_hash] = (key, value)
        self.__elem_count += 1

        if self.__elem_count / len(self.__list) >= HashDict.MAX_LOAD_FACTOR:
            self.__rehash()


    def __rehash(self):
        temp = self.__list

        self.__list = List.repeat(self.next_capacity(), None)

        self.__elem_count = 0

        for elem in temp:
            if elem != None:
                self.set(elem[0], elem[1])
        

    def remove(self, key: str) -> Any:
        pass


    def from_array(array):
        pass