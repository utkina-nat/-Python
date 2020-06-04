'''Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
 одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.'''

from abc import ABC, abstractclassmethod


class AbstractClothes(ABC):
    @property
    @abstractclassmethod
    def _type(self):
        pass

    @abstractclassmethod
    def name(self):
        pass

    @abstractclassmethod
    def type(self):
        pass

    @abstractclassmethod
    def calc_fabric_consumption(self):
        pass


class Coat(AbstractClothes):
    _type = 'Пальто'

    def __init__(self, name, size):
        self._name = name
        self._size = size

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    def calc_fabric_consumption(self):
        return self._size / 6.5 + 0.5


class Suit(AbstractClothes):
    _type = 'Костюм'

    def __init__(self, name, height):
        self._name = name
        self._height = height

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    def calc_fabric_consumption(self):
        return 2*self._height + 0.3


class AllClothes:
    def __init__(self):
        self._clothes = []

    def add(self, item):
        assert isinstance(item, AbstractClothes), "Error! Wrong type of data to add"
        self._clothes.append(item)

    def calc_total_consumption(self):
        return sum(c.calc_fabric_consumption() for c in self._clothes)


light_coat = Coat("Лёгкое осеннее пальто", 30)
print(f"Название: {light_coat.name}, тип: {light_coat.type}, \n"
      f"Ткани затрачено на производство: {light_coat.calc_fabric_consumption():.2f} м.\n")

winter_coat = Coat("Тёплое зимнее пальто", 30)
print(f"Название: {winter_coat.name}, тип: {winter_coat.type}, \n"
      f"Ткани затрачено на производство: {winter_coat.calc_fabric_consumption():.2f} м.\n")

business_suit = Suit("Деловой костюм", 1.90)
print(f"Название: {business_suit.name}, тип: {business_suit.type}, \n"
      f"Ткани затрачено на производство: {business_suit.calc_fabric_consumption():.2f} м.\n")


all_clothes = AllClothes()
all_clothes.add(light_coat)
all_clothes.add(winter_coat)
all_clothes.add(business_suit)
print(f"Ткани затрачено на производство всей одежды: {all_clothes.calc_total_consumption():.2f} м.")