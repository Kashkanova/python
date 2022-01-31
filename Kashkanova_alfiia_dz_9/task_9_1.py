import time

class TrafficLight:
    def __init__(self):
        self.__color = 'red'
        self.__duration = {'red' : 7,
                           'yellow' : 2,
                           'green' : 10}
    def running(self,color):
        if color in self.__duration:
            self.__color = color
            print(f'switching to {self.__color}, wait time is {self.__duration[self.__color]} s')
            time.sleep(self.__duration[self.__color])


light = TrafficLight()
light.running('red')
light.running('yellow')
light.running('green')
