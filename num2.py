from abc import ABC, abstractmethod

class Cloth(ABC):

    @abstractmethod
    def expend(self):
        """Посчитать количество ткани"""


class Dress(Cloth):

    def __init__(self, size, height):
        self.size = size
        self.height = height

    def expend(self):
        return (self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)

class Coat(Dress):

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def expend(self):
        return self.size / 6.5 + 0.5


class Suit(Dress):

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def expend(self):
        return self.height * 2 + 0.3


dress = Dress(40, 20)
coat = Coat('Пальто', 40)
suit = Suit('Костюм', 20)
print(coat.expend())
print(suit.expend())
print(dress.expend())
