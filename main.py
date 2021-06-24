class Cells:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cells(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Операция вычитания невозможна!')


    def __mul__(self, other):
        return Cells(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cells(round(self.quantity // other.quantity))


    def make_order(self, cells_in_a_row):
        row = ''
        for i in range(int(self.quantity / cells_in_a_row)):
            row += f'{"*" * cells_in_a_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_a_row)}'
        return row


cells_1 = Cells(88)
cells_2 = Cells(7)
print(cells_1)
print(cells_1 + cells_2)
print(cells_2 - cells_1)
print(cells_2.make_order(5))
print(cells_1.make_order(10))
print(cells_1 / cells_2)