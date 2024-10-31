from __future__ import annotations


# class LibraryItem:
#     def __init__(self, id: str):
#         self.__id: str = id

#     def take(self, book):
#         self.book = id
#         return (' Взять на время')
    

#     def revert(self):
#         return(' Вернуть ')

            
    
#     def __str__(self) -> str:
#         return f' '
        
        
# class Book(LibraryItem):
#     def __init__(self, id: str, author : str, info : str = str):
#         super().__init__(id)
#         self.__author : str = author
#         self.__info : str = info






# class Magazine(LibraryItem):



class Videolibrary:
    def __init__(self, id : int, name: str, director : str, duration : int, rented : bool = False):
        self.__id : int = id
        self.__name : str = name
        self.__director : str = director
        self.__duration : int = duration
        self.__taken : bool = rented
      
    @property  
    def id(self):
        return self.__id

    def is_taken(self):
        return self.__taken
    
    def change_status(self):
        self.taken = not self.taken

    def __str__(self) -> str:
        return f'{self.__id} : {self.__director} - {self.__name} '




class Movies(Videolibrary):
    def __init__(self, id: int, name: str, director : str, ):
        super().__init__(id, name)
        self.__director : str = director
     
    def __str__(self) -> str:
        return super().__str__() 

class Serials(Videolibrary):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
      

class Documentaries(Videolibrary):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)        