
class Matrix:
    def __init__(self, matr1):
        self.matr1 = matr1

    def __add__(self, other):
        result = [[self.matr1[i][j] + other.matr1[i][j] for j in range (len(self.matr1[0]))] for i in range(len(self.matr1))]
        return Matrix(result)
    def __str__(self):
        return ('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.matr1]))



matrix1 = Matrix([[1,2,3],[2,1,3]])
matrix2 = Matrix([[4,5,7],[6,2,2]])

print(matrix1+matrix2)

