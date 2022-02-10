class My_list_numbers(Exception):
    def __init__(self, number):
       self.number = number
my_list = []
while True:
    try:
        number = input('Введите число в список:')
        if number == 'stop':
            break
        if not number.isdigit():
            raise My_list_numbers(number)
        my_list.append(int(number))
    except My_list_numbers:
        print('Не число!')
print(my_list)
