
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула {direction}'

    def show_speed(self, speed):
        return f'Текущая скорость {self.name} {speed} км/час'


class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print('Превышена скорость')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 40:
            print('Превышена скорость')


class PoliceCar(Car):
    pass


moskvich = TownCar(80, 'Зеленый', 'Москвич', False)
ferrari = SportCar(300, 'Красный', 'Ferrari', False)
kamaz = WorkCar(50, 'Оранжевый', 'Камаз', False)
lada = PoliceCar(150, 'Белая', 'Полицейская лада', True)

print(f'{moskvich.go()} \n {moskvich.turn("Направо")} \n {moskvich.stop()}')
print(moskvich.show_speed(70))

