
class Warehouse:

    def __init__(self):
        self.dict_office_equipment = {}
        self.list_office_equipment = []

    def __add__(self, other):
        self.dict_office_equipment[other.name] = other.price, other.year
        self.list_office_equipment.append(self.dict_office_equipment)

    #def __del__(self, other):
        #del self.dict_office_equipment[other.name]

class Office_equipment:

    def __init__(self, name, price, year):
        self.name = name
        self.price = int(price)
        self.year = int(year)

    def __str__(self):
        return f'{self.name}-{self.price}-{self.year}'

class Printer(Office_equipment):

    def action(self):
        return f'Печатает'

class Xerox(Office_equipment):

    def action(self):
        return f'Копирует'

class Scaner(Office_equipment):

    def action(self):
        return f'Сканирует'


warehouse = Warehouse()
printer1 = Printer('HP', 20000, 2021)
warehouse.__add__(printer1)
printer2 = Printer('Canon', 2000, 2021)
warehouse.__add__(printer2)
scaner = Scaner('Hp', 3000, 2022)
warehouse.__add__(scaner)
print(warehouse.list_office_equipment)
#warehouse.__del__(printer2)



