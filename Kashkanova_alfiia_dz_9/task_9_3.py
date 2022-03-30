

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position
        self._income = {"wage" : wage,
                        "bonus" : bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'полное имя сотрудника:  {self.name} {self.surname} ')
    def get_total_income(self):
        total_sum = self._income["wage"]+self._income["bonus"]
        print(f'доход сотрудника составляет {self._income["wage"]}, с учетом премии {total_sum}')

user1 = Position('dima', 'ivanov', 'повар', 5000, 2568)
user1.get_full_name()
user1.get_total_income()