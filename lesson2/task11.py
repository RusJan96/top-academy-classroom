from __future__ import annotations
import math

from abc import abstractmethod

class Figure:
    @abstractmethod
    def get_area(self)-> float:
        raise NotImplementedError(' Требуется переопределить метод get_area')
    

class Rectangle(Figure):
    def __init__(self, length : float, width : float):
       self.__lenght : float = length
       self.__width : float = width

    def get_area(self):
     return self.__lenght * self.__width
        

class Circle(Figure):
    def __init__(self, radius : float) -> None:
        self.__radius : float = radius
    
    def get_area(self,):
        return math.pi *  self.__radius ** 2
        

a = Rectangle(2, 6)
print(a.get_area())

b = Circle(5)
print(b.get_area())

