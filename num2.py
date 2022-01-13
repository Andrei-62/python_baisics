
class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def culculation(self):
        mass_asfalta = 25
        width = int(input('Введите толщину асфальта - '))
        print(self.length * self.width * mass_asfalta * width)


road = Road(20, 10)
road.culculation()
