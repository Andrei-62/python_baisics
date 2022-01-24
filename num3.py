class ExceptErorr(Exception):
    def __init__(self, *args):
        self.my_list = []

    def check_to_int(self):
        print('Для завершения программы напиши stop')
        while True:
            val = input('Введите число - ')
            if val == 'stop':
                break
            try:
                val == int(val)
                self.my_list.append(val)
            except:
                print('Это не число!')
        print(self.my_list)


exceptErorr = ExceptErorr()
exceptErorr.check_to_int()
