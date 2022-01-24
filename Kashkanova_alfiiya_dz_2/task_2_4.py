
professions = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for profession in professions:
    profession_name = profession.split()[-1].lower().capitalize()
    print('Привет, ' + profession_name + '!')
