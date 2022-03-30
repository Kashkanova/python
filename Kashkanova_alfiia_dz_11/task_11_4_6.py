class Office_equ():
    def __init__(self, format, is_color):
        self.format = format
        self.is_color = is_color
    def __str__(self):
        return f'{self.format}'
    def __eq__(self, other):
        return (self.format, self.is_color) == (other.format, other.is_color)
    def __hash__(self):
        return hash((self.format, self.is_color))

class Sklad():

    def __init__(self):
        self.dict_equ = {'sklad': {}}

    def add (self, equipment, quantity):
        if equipment not in self.dict_equ['sklad']:
            self.dict_equ['sklad'][equipment] = quantity
        else:
            self.dict_equ['sklad'][equipment] += quantity

    def transfer (self, equipment, division, quantity):
        if division not in  self.dict_equ:
            self.dict_equ[division] = {}
        if equipment in self.dict_equ['sklad']:
            if self.dict_equ['sklad'][equipment] >= quantity:
                self.dict_equ['sklad'][equipment] -= quantity
                if equipment not in self.dict_equ[division]:
                    self.dict_equ[division][equipment] = quantity
                else:
                    self.dict_equ[division][equipment] += quantity
    def __str__(self):
        return f' {self.dict_equ}'
    def print_equ(self):
        for division in self.dict_equ:
            print(division)
            for item in self.dict_equ[division]:
                print(f'{item}, {self.dict_equ[division][item]} шт')


class Printer(Office_equ):
    def __init__(self, format, is_color, type_tec): #type - matrix, laser, jet
        super().__init__(format, is_color)
        self.type_tec = type_tec
    def __eq__(self, other):
        return (self.format, self.is_color, self.type_tec) == (other.format, other.is_color, other.type_tec)
    def __hash__(self):
        return hash((self.format, self.is_color, self.type_tec))
    def __str__(self):
        return f' {self.__class__.__name__}: format {self.format}, color {self.is_color}, type_tec {self.type_tec}'

class Scaner(Office_equ):
    def __init__(self, format, is_color, auto_feed): #auto, hand
        super().__init__(format, is_color)
        self.auto_feed = auto_feed
    def __eq__(self, other):
        return (self.format, self.is_color, self.auto_feed) == (other.format, other.is_color, other.auto_feed)
    def __hash__(self):
        return hash((self.format, self.is_color, self.auto_feed))
    def __str__(self):
        return f' {self.__class__.__name__}: format {self.format}, color {self.is_color}, auto_feed {self.auto_feed}'

class Xerox(Office_equ):
    def __init__(self, format, is_color, auto_feed, type_tec ):
        super().__init__(format, is_color)
        self.auto_feed = auto_feed
        self.type_tec = type_tec
    def __eq__(self, other):
        return (self.format, self.is_color, self.auto_feed, self.type_tec) == (other.format, other.is_color, other.auto_feed, other.type_tec)
    def __hash__(self):
        return hash((self.format, self.is_color, self.auto_feed, self.type_tec))
    def __str__(self):
        return f' {self.__class__.__name__}: format {self.format}, color {self.is_color}, auto_feed {self.auto_feed}, type_tec {self.type_tec}'

my_sklad = Sklad()
my_sklad.add(Printer('A4', True, 'laser'), 10)
my_sklad.add(Xerox('A4', True, 'auto', 'jet'), 5)
my_sklad.add(Scaner('A5', False, 'auto'), 8)
my_sklad.add(Printer('A4', True, 'jet'), 3)
my_sklad.add(Scaner('A1', True, 'hand'), 10)
my_sklad.transfer(Xerox('A4', True, 'auto', 'jet'), 'otdel1', 2)
my_sklad.transfer(Scaner('A5', False, 'auto'), 'otdel3', 3)
print(my_sklad.print_equ())
