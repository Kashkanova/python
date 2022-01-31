
class Car():
    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name.capitalize()
        self.is_police = False
    def go(self, speed):
        self.speed = speed
        print(f'Поехала машина {self.name} {self.color} цвета ')
    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} {self.color} цвета остановилась ')
    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name} повернула на{self.direction}')
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} составляет {self.speed} миль ')

class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print(f'Текущая скорость автомобиля {self.name} превышена = {self.speed} миль ')
class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print(f'Текущая скорость автомобиля {self.name} превышена = {self.speed} миль ')

class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True


car1 = Car( 'красного', 'lada')
car1.go(65)
car1.stop()
car1.turn('право')
car1.show_speed()
car2 = WorkCar( 'черного', 'audi')
car2.go(45)
car2.show_speed()
car3 = PoliceCar('синего', 'mazda')
car3.go(80)
car3.show_speed()
car4 = TownCar('желтого', 'opel')
car4.go(85)
car4.turn('лево')
car4.show_speed()
car4.stop()