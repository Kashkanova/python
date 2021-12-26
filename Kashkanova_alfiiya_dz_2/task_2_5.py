import math

prices = [57.8, 46.51, 97, 25.3, 45.03, 78, 96.2, 12, 85.1, 47.4, 6.63]
prices_old_id = id(prices)
for price in prices:
    cost = price * 100
    rub =math.floor (cost // 100)
    kop = math.floor (cost % 100)
    print(f' {rub:02d} рублей {kop:02d} копеек')
# отсортируем по возрастанию
prices.sort()
print(prices)
# сравним старый и новый id
prices_id = id(prices)
if prices_old_id == prices_id:
    print('the same id')
# сортируем список по убыванию
prices_2 = prices[::-1]
print(prices_2)
# выводим 5 самых высоких цен
prices_high_5 = prices_2 [:5]
print(prices_high_5)