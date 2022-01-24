class DivisionErorr(Exception):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def divide_by_null(numerator, denominator):
        try:
            denominator != 0
            return numerator / denominator
        except:
            return f"Делить на ноль нельзя"



print(DivisionErorr.divide_by_null(10, 10))
