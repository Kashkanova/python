class Stationery:
    def __init__(self):
        self.title = ''
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self):
        self.title = 'Pen'
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Pencil'
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def __init__(self):
        self.title = 'Handle'
    def draw(self):
        print('Запуск отрисовки маркером')

tool = Stationery()
tool.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
print(handle.title)


