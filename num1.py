from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        count = 7
        for i in range(len(self.__color)):
            print(self.__color[i])
            sleep(count)
            count -= 2


t = TrafficLight()
t.running()
