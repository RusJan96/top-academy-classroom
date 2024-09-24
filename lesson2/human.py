

from __future__ import annotations
class Human:
    def __init__(self, name: str, age : int):
        self._name: str = Human._validate_name(name)
        self._age: int = Human._validate_age(age)

    @staticmethod
    def _validate_name(name: str) -> str:
        if name.isalpha():
            return name
        raise Exception(' Имя должно содержать только буквы.')

    @staticmethod
    def _validate_age(age: int) -> int:
        if 0 < age <= 180:
            return age
        raise Exception(' Возраст должен быть от 1 до 180.')

    def __str__(self):
        return f'{self._name} ({self._age})'   
    


class Builder(Human):
    def __init__(self,name : str, age: int, post: str, experience: int):
        super().__init__(name, age)
        self._post: str = Builder._validate_post(post)
        self._experience: int = Builder._validate_experience(experience)

    @staticmethod
    def _validate_post(post: str) -> str:
        if post.isalpha():
            return post
        raise Exception(' должность должна содержать только буквы.')

    @staticmethod
    def _validate_experience(experience: int) -> int:
        if 0 < experience <= 20:
            return experience
        raise Exception(' Опыт работы должен быть от 1 до 20 лет.')


class Pilot(Human):
   def __init__(self, name: str, age: int, health : int):
       super().__init__(name, age)
       self.__health = health

   def is_healthy(self) -> bool:
       if self.__health <10:
           return False
       return True
            

class Sailor(Human):
   pass