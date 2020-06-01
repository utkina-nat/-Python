'''Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т'''

class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width
    def count_weight_asphalt(self, weight = 25, thickness = 0.5):
        return self._lenght * self._width * weight * thickness


user_1 = Road(20, 50)
print(user_1.count_weight_asphalt())