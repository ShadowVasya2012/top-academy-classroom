class City: 
    def __init__(self, name, reg_name, country_name, population, mail_index, number_code) -> None:
        self.name = name
        self.reg_name = reg_name
        self.country_name: str = country_name
        self.population = population
        self.mail_index: str = mail_index
        self.number_code = number_code
    
    
    def print(self):
        print('Выводим город: ')
        print(f'Название города {self.name}')
        print(f'Название региона {self.reg_name}')
        print(f'Название страны {self.country_name}')
        print(f'Население города {self.population}')
        print(f'Почтовый индекс города {self.mail_index}')
        print(f'Телефонный код города {self.number_code}')
        
piter: City = City('Питер', 'Не ебу', 'Россия', 'Много', 'Тоже есть какой то', '+7')
piter.print()
    