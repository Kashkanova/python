

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa_road(self, thickness, massa = 25):
        massa_asf = self._length * self._width * massa * thickness//1000
        print(f'Масса асфальта равна {massa_asf} тонн')

massa_asfalta = Road(5000, 20)
massa_asfalta.massa_road(5)
