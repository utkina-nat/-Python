'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''

class Car:
    speed_limit = None
    def __init__(self, color,name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False
        self.direction = None

    def go(self, go_speed=None):
        self.speed = go_speed or self.speed
        if self.speed:
            print(f'Машина {self.name} едет.', end=' ')
            self.show_speed()
        else:
            print(f'Машина не едет, т.к не указана скорость')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name} повернула {self.direction}.', end=' ')
        self.show_speed()

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч.')


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        super().show_speed()
        if self.speed > self.speed_limit:
            print(f'ПРЕВЫШЕНИЕ СКОРОСТИ! Снизьте скорость на {self.speed - self.speed_limit} км/ч')


class PoliceCar(Car):
    speed_limit = 60

    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True
        self.flasher_is_on = False

    def show_speed(self):
        super().show_speed()
        if self.speed > self.speed_limit and not self.flasher_is_on\
                or self.speed < self.speed_limit and self.flasher_is_on:
            self.flasher_switch()

    def flasher_switch(self):
        if self.flasher_is_on:
            self.flasher_is_on = False
            print('Проблесковые маячки выключены.')
        else:
            self.flasher_is_on = True
            print('Проблесковые маячки включены.')


town_car = TownCar('красная', 'smart')
print(f'Имя: {town_car.name} | Цвет: {town_car.color} | Текущая скорость: {town_car.speed} | '
      f'Полицейская: {town_car.is_police} | Допустимая скорость: {town_car.speed_limit}')

town_car.go()
town_car.go(100)
town_car.go(50)
town_car.turn('назад')
town_car.stop()
town_car.show_speed()
town_car.go()

print('_' * 50)