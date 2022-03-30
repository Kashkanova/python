class My_exc(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data1 = int(input('Введите первое число: '))
inp_data2 = int(input('Введите второе число: '))

try:
    if inp_data2 == 0:
        raise My_exc('На ноль делить нельзя! ')
    result = inp_data1 / inp_data2
except My_exc as err:
    print(err)
else:
    print(f' Ваш результат: {result}')



