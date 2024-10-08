from __future__ import annotations


class Item:
    def __init__(self, value: int, nxt: Item | None = None):
        self.value: int = value
        self.next: Item = nxt


b = Item(2, None)
a = Item(1, None)


class LinkedList:
    def __init__(self, item: Item):
        self.__item: Item  | None = None
        self.__current = None
        
    def add(self, value : int):
       if self.__item is None:
        self.__item = Item(value) 

        pass


    def remove(self):
        pass

    def get(self):
        pass   