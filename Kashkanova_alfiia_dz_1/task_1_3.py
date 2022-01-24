
for i in range(1,101):
    ending = ''

    if i % 10 == 1:
        pass

    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        ending = 'а'

    else:
        ending = 'ов'
    print(i,'процент'+ ending)


