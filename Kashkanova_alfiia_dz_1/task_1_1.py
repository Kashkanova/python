import random
duration = random.randint(1,500000) #кол-во сек генерирует комп
print(duration)

days = duration // 86400 #кол-во сек в 1 дне = 86400
duration = duration -(days * 86400) # нахожу остаток секунд на ч+м+с
hours = duration // 3600
duration = duration - (hours * 3600) # # нахожу остаток секунд на м+с
minutes = duration // 60
secunds = duration  % 60

print(days, ' дн', hours, ' час', minutes, ' мин',  secunds, ' сек')