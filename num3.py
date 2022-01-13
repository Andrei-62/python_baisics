
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']



man = Position('Иван', 'Иванов', 'Гинеколог', 20000, 10000)
print(f'Зарплата сотрудника {man.get_full_name()} составляет {man.get_total_income()} у.е.')

