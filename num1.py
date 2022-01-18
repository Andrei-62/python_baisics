
class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for i in self.my_list:
            for j in i:
                print(j, end=' ')
            print()

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix.__str__(self)


matrix1 = Matrix([[1, 2, 3], [2, 3, 4], [4, 5, 6]])
matrix2 = Matrix([[2, 3, 4], [2, 2, 4], [2, 3, 4]])
matrix1.__add__(matrix2)
