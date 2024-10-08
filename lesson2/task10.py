from __future__ import annotations

class Person:
    def __init__(self, name: str, age: int):
        self.__name: str = name
        self.__age: int = age
        
    def __str__(self) -> str:
        return f' Имя : {self.__name}  Возраст : {self.__age}'  


class Student(Person):
    def __init__(self, name: str, age: int, educational_institution : str, average_score: float) -> None:
       super().__init__(name, age)
       self.__educational_institution : str = educational_institution
       self.__average_score: float = average_score

    def __str__(self) -> str:
        
        return super().__str__() + f' Учебное заведение : {self.__educational_institution}  Средний балл : {self.__average_score}'  
    
h1=Student(' Игорь', 17, ' Школа № 5', 4.5 )    
print(h1)
