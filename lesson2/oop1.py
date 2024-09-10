

class City :
    

    def __init__(self, city : str, region : int, country : str, number_of_people : int, index : int, phone_kod : int):
        self.city = city
        self.region = region
        self.country = country
        self.number_of_people = number_of_people
        self.index = index
        self.phone_kod = phone_kod
        

    def print(self):
        print(' Название города', self.city)    
        print(' Регион ')
        print(' Страна')
        print(' Количество людей в городе')
        print(' Почтовый индекс')
        print(' телефонный код города')
        

Krasnoyarsk: City = City('Красноярск', '124', ' Россия', ' 2 846 120', '660000', ' (391)') 
Krasnoyarsk.print()       


Tomsk: City = City('Томск', '70', ' Россия', ' 545 391', '634000', ' (382-2)') 
Tomsk.print()