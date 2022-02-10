
class Data:

    def __init__(self, date_str):
       self.date_str = date_str
    @classmethod
    def get_date(cls,date_str):
        d = date_str.split('-')
        day = int(d[0])
        month = int(d[1])
        year = int(d[2])
        return (day, month, year)
    @staticmethod
    def valid_date(args):
        days = {1: 31,
                2: [28,29],
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31
        }
        if 1900 < args[2] < 2099:
            print('год валиден')
        else:
             print('год не валиден')
        if args[1] == 2:
            if args[2]  % 4 == 0 and (args[2] % 100 != 0 or args[2] % 400 == 0):
                days[args[1]] = 29
                print('год високосный')
            else:
                days[args[1]] = 28
                print('год невисокосный')
        if 0 < args[0] <= days[args[1]]:
            print('дни валидны')
        else:
            print('дни не валидны')
        if 0 < args[1] <= 12:
            print('месяцы в порядке')
        else:
            print('месяцы не в порядке')

Data.get_date('4-2-2022')
print(Data.get_date('4-2-2022'))
Data.valid_date(Data.get_date('29-02-2020'))
