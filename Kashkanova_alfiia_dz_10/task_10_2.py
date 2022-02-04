class Wear:
    def __init__(self,V,f_c = 0, type_of_wear=''):
        self.size = V
        self.type_of_wear = type_of_wear
        self.f_c = f_c
    def __add__(self, other):
        return ( Wear(0, self.f_c + other.f_c))
    def __str__(self):
        return f'Общее количество ткани на  {self.type_of_wear}: {self.f_c}'

    @property
    def my_metod(self):
        print(self)

class Coat(Wear):
    def __init__(self, V):
        super().__init__(V,V/6.5 + 0.5,'пальто')


class Costume(Wear):
    def __init__(self, H):
        super().__init__(H, 2 * H + 0.3, 'костюм')

coat = Coat(10)
costume = Costume(41)
print(coat + costume)
print(costume)

coat.my_metod
