from __future__ import annotations


class Passport:
    def __init__(self,name: str, surname: str, number: int, series: int, date_of_issue: int, country: str, ) -> None:
        self._name : str = name
        self._surname : str = surname
        self._nubmer : str = number
        self._series : str = series
        self._date_of_issue : str = date_of_issue
        self._country : str = country

    @staticmethod
    def _validate_name(name: str) -> str:
        if name.isalpha():
            return name
        raise Exception(' Имя должно содержать только буквы.')
    

    @staticmethod
    def _validate_name(surname: str) -> str:
        if surname.isalpha():
            return surname
        raise Exception(' Имя должно содержать только буквы.')
    
    @staticmethod
    def _validate_number(number: int) -> int:
        if number:
            return number
        raise Exception(' Номер должен содержать только цифры.')
    
    
    @staticmethod
    def _validate_series(series: int) -> int:
        if  series:
            return series
        raise Exception(' Серия  должена содержать только цифры.')
    
    @staticmethod
    def _validate_date_of_issue(date_of_issue: int) -> int:
        if not date_of_issue.isalpha():
            return date_of_issue
        raise Exception(' Дата  должена содержать только цифры.')
    
    @staticmethod
    def _validate_country(country: str) -> str:
        if country.isalpha():
            return country
        raise Exception(' Страна  должена содержать только буквы.')
   

    def __str__(self) -> str:
         return f'Имя : {self._name}, Фамилия : {self._surname}, Номер паспорта : {self._number}, Серия паспорта: {self._series}, Дата выдачи : {self._date_of_issue}, Старна : {self._country}'  


class Zagran():
    pass


p1 = Passport('Кирилл', 'Иванов', 6913, 809456, 07.092003, 'Россия ' )
print(p1)