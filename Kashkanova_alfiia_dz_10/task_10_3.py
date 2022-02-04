
class Cell:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        return Cell (self.n + other.n)
    def __sub__(self, other):
        if self.n > other.n:
            return Cell(self.n - other.n)
        else:
            print('разность меньше нуля')
    def __mul__(self, other):
        return Cell(self.n * other.n)
    def __str__(self):
        return f' Результат операции : {self.n}'
    def __floordiv__(self, other):
        return Cell(self.n // other.n)
    def __truediv__(self, other):
        return Cell(self.n / other.n)
    def make_order(self, x):
        result = ''
        for i in range(self.n):
            if i !=0 and i % x == 0:
                result +='\n'
            result +='*'
        return result



cell1 = Cell(5)
cell2 = Cell(17)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1 // cell2)
print(cell2.make_order(5))