# 19.09

# задание 1
from __future__ import annotations

class Number:
    def __init__(self, value: int | float) -> None:
        self.__value: int | float = value

    def __str__(self) -> str:
        return str(self.__value)    

    def __add__(self, other: Number) -> Number:
        return Number(self.__value + other.__value)
    

    def __sub__(self, other: Number) -> Number:
        return Number(self.__value - other.__value)
    
 

    def __mul__(self, other: Number) -> Number:
        return Number(self.__value * other.__value)
    

    def __truediv__(self, other: Number) -> Number:
        return Number(self.__value / other.__value)
    



a = Number(2)
b = Number(5)

print (a + b)
print (a - b)
print (a * b)
print (a / b)