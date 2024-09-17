

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
        print(' Регион ', self.region)
        print(' Страна',self.country)
        print(' Количество людей в городе',self.number_of_people)
        print(' Почтовый индекс',self.index)
        print(' телефонный код города',self.phone_kod )
        

Krasnoyarsk: City = City('Красноярск', '124', ' Россия', ' 2 846 120', '660000', ' (391)') 
Krasnoyarsk.print()    
print(' ')   


Tomsk: City = City('Томск', '70', ' Россия', ' 545 391', '634000', ' (382-2)') 
Tomsk.print()