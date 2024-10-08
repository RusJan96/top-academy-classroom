from __future__ import annotations


class Book:
    def __init__(self, name : str, author : str, year: int):
        self.__name : str = name
        self.__author: str = author
        self.__year: int = year
    
   
    def change_year(self, year : int):
        if not 865 <= year <= 2024:
          raise ValueError(' Введите корректную дату издания') 
        self.__year = year


    def get_info(self):
         print(self)

    def __str__(self) -> str:
        return f'Название :{self.__name} Автор :{self.__author} Год издания : {self.__year}'

book = Book( ' Договориться можно обо всем', 'Гэвин Кеннеди', '2007')
book.get_info()
book.change_year(2009)
book.get_info()