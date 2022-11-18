class Node:
    def __init__(self, next, elem):
        self.next = next
        self.elem = elem


class List:
    def __init__(self):
        self.head = None


    def insert(self, elem): # C
        new_elem = Node(None, elem) # инициализация нового узла

        if self.head is None: # если указатель на начало списка None, то мы просто добавляем первый (нулевой по индексу) узел в список
            self.head = new_elem
            return
        
        curr_elem = self.head # иначе, ищем последний узел: присваиваем переменной указатель на первый узел, который точно есть

        while curr_elem.next: # пока указатель на следующий узел не None
            curr_elem = curr_elem.next # переходим на следующий узел

        curr_elem.next = new_elem # после цикла указатель текущего узла указывает на None, и мы просто сцепляем этот указатель на новый узел
    
    def find_node(self, index):
        curr_elem = self.head
        
        count = 0

        while count < index:
            curr_elem = curr_elem.next
            count += 1

        return curr_elem



    def get(self, index): # R
        if index > self.length() - 1: # проверка на валидность введенного индекса
            raise Exception(f"Index {index} is out of bound! List length: {self.length()}")

        # count = 0

        # # Цикл №1
        # while count < index: # идём до индекса: ввели 0, то в цикл не входим, возвращаем нулевой элемент
        #     curr_elem = curr_elem.next
        #     count += 1
        
        return self.find_node(index).elem


    def length(self): # R
        if self.head is None: # если указатель на начало списка None, то в списке ноль узлов - его длина 0
            return 0
        

        curr_elem = self.head # текущий элемент равен первому узлу списка

        count = 1 # один элемент в списке точно есть
        
        while curr_elem.next: # пока указатель текущего элемента на следующий не None
            curr_elem = curr_elem.next # переходим на следующий узел
            count += 1
        
        return count
    

    def set(self, index, elem): # U
        if index > self.length() - 1: # проверка на валидность введенного индекса
            raise Exception(f"Index {index} is out of bound! List length: {self.length()}")

        curr_elem = self.head # текущий элемент равен первому узлу списка

        count = 0

        # Цикл №2
        while count < index: # идём до нужного индекса: если 0, то в цикл не входим; если 1 и более, то входим минимум один раз
            curr_elem = curr_elem.next
            count += 1
        
        curr_elem.elem = elem # возвращаем элемент


    def remove(self, index): # D
        # 1) List( head = None )any Node.remove() ---> Error! | пустой список

        # 2) List( head = Node №1.remove -> Node №2 -> ... -> None) | удаление элемента по индексу 0

        # 3) List( head = Node№1 -> ... -> Node №N - 1 -> Node №N.remove -> Node №N + 1... -> None ).remove(index = [0; self.length() - 1]) --> Ok! | общий случай
        # 4) List( head = Node №1 -> Node №2.remove -> Node №3 -> Node №4 -> None)
        #          index     0             1               2          3


        len = self.length() # получаем длину списка

        if index > len - 1 or len == 0: # случай, если индекс за пределами длины списка или у нас пустой список
            raise Exception(f"Index {index} is out of bound! List length: {self.length()}")
        
        if index == 0: # если нужно удалить первый элемент, то необходимо просто передвинуть указатель на первый узел на следующий узел
            self.head = self.head.next
            return

        # curr_elem = self.head # текущий элемент равен первому узлу списка

        # count = 0

        # # Цикл №3(?)
        # while count < index - 1: # пока не дойдем до индекса элемента, ПРЕДШЕСТВУЮЩЕГО удаляемому
        #     curr_elem = curr_elem.next
        #     count += 1

        curr_elem.next = curr_elem.next.next # указатель текущего узла на следующий узел равен двойному шагу по связи текущего узла 
        #                                               (удалённый элемент наверное сам удаляется из памяти)
    

    def print(self):
        if self.head is None: # если указатель на начало списка None, то в списке ноль узлов - он пустой
            print(f"[]")
            return

        curr_elem = self.head # текущий элемент равен первому узлу списка
        print(f"[{curr_elem.elem}", end='') # печатаем его

        while curr_elem.next: # пока указатель на следующий узел не None
            curr_elem = curr_elem.next # переходим на следующий узел
            print(f", {curr_elem.elem}", end='') # печатаем элемент
        
        print(f"]")


        # curr_elem = self.head # текущий элемент равен первому узлу списка

        # print(f"[", end='')
        # while curr_elem:
        #     print(f" {curr_elem.elem} ", end='')
        #     curr_elem = curr_elem.next
        # print(f"]")
    

    def find(self, elem):
        if self.head is None: # если указатель на начало списка None, то в списке ноль узлов - он пустой
            return None

        curr_elem = self.head # текущий элемент равен первому узлу списка

        count = 0

        # List( head = Node №1 -> Node №2 -> Node №3 -> Node №4 -> None)

        if curr_elem.elem == elem:
            return count

        while curr_elem: # интересный момент: пока текущий элемент не None (а не его поле next)
            if curr_elem.elem == elem:
                return count
            
            curr_elem = curr_elem.next
            count += 1

        return None

l = List()

# Методы: insert(elem), get(index), length(), set(index, elem), remove(index), print(), find(elem)








# -----------
# Пустой список
# l.print()

# print(l.get(0))
# print(l.get(1))

# print(l.length())

# l.set(0, 'a')

# l.remove(0)

# print(l.find('a'))
# -----------
# Список из одного элемента
# l.insert('a')
# l.print()

# print(l.get(0))
# # print(l.get(1))

# print(l.length())

# print("\nЗамена элемента:")
# l.set(0, 'b')
# print(l.get(0)) 
# l.print()

# print("\nУдаление элемента:")
# l.remove(0)
# l.print()

# print("\nПоиск элемента")
# l.insert('a')
# l.print()
# print(l.find('a'))
# -----------
# Список из множества элементов
# l.insert('p')
# l.insert('o')
# l.insert('n')
# l.insert('y')

# l.print()

# print("Длина:", l.length())

# print(l.get(2))

# l.set(3, 'k')
# l.print()

# l.remove(3)
# l.print()
# l.insert('y')
# l.print()

# print(l.find('y'))