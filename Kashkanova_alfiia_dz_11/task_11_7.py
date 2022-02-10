class Complex_number():
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Complex_number(self.n + other.n)

    def __mul__(self, other):
        return Complex_number(self.n * other.n)

    def __str__(self):
        return f' Результат операции : {self.n}'

number1 = Complex_number(5 + 3j)
number2 = Complex_number(-8 + 2j)
print(number1 + number2)
print(number1 * number2)
