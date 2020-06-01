'''Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        if self.title:
            print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        if self.title:
            print(f'Запуск отрисовки ручкой {self.title}.')


class Pencil(Stationery):
    def draw(self):
        if self.title:
            print(f'Запуск отрисовки карандашом {self.title}.')


class Handle(Stationery):
    def draw(self):
        if self.title:
            print(f'Запуск отрисовки маркером {self.title}.')


pen_1 = Pen('LAMY')
pen_1.draw()

pencil_1 = Pencil('Kohinoor')
pencil_1.draw()

handle_1 = Handle('Copic')
handle_1.draw()
