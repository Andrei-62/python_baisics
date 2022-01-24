
class Data:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def extract(cls, d_m_y):
        my_list = []
        for i in d_m_y.split('-'):
            my_list.append(int(i))
        return my_list

    @staticmethod
    def valid(d_m_y):
        my_data = Data.extract(d_m_y)
        if 31 >= my_data[0] >= 1 and 12 >= my_data[1] >= 1 and 2022 >= my_data[2] >= 0:
            return f'Верная дата'
        else:
            return f'Неверная дата'


data1 = Data('20-02-2021')
print(Data.extract('20-02-2021'))
print(Data.valid('30-12-2022'))

