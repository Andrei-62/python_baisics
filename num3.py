
class Cell:

    def __init__(self, count):
        self.count = int(count)

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if self > other:
            return self.count - other.count
        if other > self:
            return other.count - self.count
        else:
            return f'Вычитание не возможно'

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count / other.count

    def __str__(self):
        return f'{self.count * "*"}'


    def make_order(self, num):
        result = ''
        for i in range(int(num / self.count)):
            result += self.__str__() + '\n'
        result += '*' * int((num % self.count))
        return result



cell1 = Cell(5)
cell2 = Cell(7)
print(cell1.__add__(cell2))
print(cell1.make_order(21))
