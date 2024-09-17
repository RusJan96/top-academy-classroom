# 17.09
# задание 4!!!


# from __future__ import annotation   

#  для классов чтобы не было ошибок!!!
class Fraction:
    def __init__(self,  numerator: int, denominator: int, int_part: int = 0) -> None:
        self.__int_part: int = int_part
        self.__num = numerator
        self.__den = denominator

    def get_num(self):
        return self.__num   
    # это чтобы получить значение - геттер!!!


    def set_num(self, value):
        if type(value) == int:
            self.__num = value 
        #  изменить значение у приватного значения!!! - это сеттер


    def add(self, fraction):
        num = self.__num * fraction.__den + fraction.__num * self.den
        den = self.__num * fraction.__den
        return Fraction(num, den)

    def subtraction(self, fraction):
        num = self.__num * fraction.__den - fraction.__num * self.den
        den = self.__num * fraction.__den
        return Fraction(num, den)


    def division(self, fraction):
        num = self.__num * fraction.__den
        den = self.__den * fraction.__num
        return Fraction(num, den)




    def multiplay(self, fraction):
        num = self.__num * fraction.__num
        den = self.__den * fraction.__den
        return Fraction(num,den)


    def __str__(self) -> str:
        num = self.__num

        if self.__num > self.__den :
            int_part = int(self.__num / self.__den)
            num -= int_part * self.__den
            return f'{int_part}({num} /{self.__den}'
        elif self.__num == self.__den:
            return str(int(self.__num/ self.__den))
        
       
        return f'{self.__num}/{self.__den}'     
    
    #  __ перед num, den - мы заносим их в приват чтоб их нельзя было изменить!!!

    def __float__(self):
        return self.__num / self.__den     
    

f1 = Fraction( 2, 3)
f2 = Fraction( 3, 5)






# print(str(f))    
# print(float(f))

print((f1))    
# print(f.den)
f3: Fraction = f1.multiplay(f2)
print(f3)
f3 : Fraction = f1.add(f2)
print(f3)
f3 : Fraction = f1.subtraction(f2)
print(f3)
f3 : Fraction = f1.division(f2)
print(f3)