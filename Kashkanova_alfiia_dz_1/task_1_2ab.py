numbers = [] #  пустой список

for number in range(1,1000,2): # генерируем числов послед-ть от 1 до 1000 с шагом 2
    numbers.append(number**3) # каждый элемент возводим в куб и добавл в список
print(numbers)

sum_total = 0 # сумма чисел списка сумма элементов которых / 7

for number in numbers: # перебираем числа в списке
    sum_numbers = 0
    n = number
    while n > 0:
        digit = n % 10 # извлекаем последнюю цифру числа
        sum_numbers = sum_numbers + digit
        n = n // 10 # извлекаем целую часть
    if sum_numbers % 7 == 0: # проверяем условие деления на 7
        sum_total = sum_total + number
print(sum_total)

numbers_2 = []
for number in numbers:
    numbers_2.append(number + 17)
print(numbers_2)
sum_total_2 = 0
for number in numbers_2:
    sum_numbers = 0
    n = number
    while n > 0:
        digit = n % 10
        sum_numbers = sum_numbers + digit
        n = n // 10
    if sum_numbers % 7 == 0:
        sum_total_2 = sum_total_2 + number
print(sum_total_2)


