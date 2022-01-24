
list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']
list_2 = []
for item in list_1:
    is_digit = item.strip('[+-]').isdigit()

    if is_digit == True:

        list_2.append('"')
        digit=int(item)
        str=f'{abs(digit):02d}'
        if item.find('+') != -1:
            str='+' + str
        elif item.find('-') != -1:
            str='-' + str

        list_2.append(str)

        list_2.append('"')
    else:
        list_2.append(item)
print(list_2)
print(' '.join(list_2))
