'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.'''

class Matrix:
    def __init__(self):
        self._user_matrix = []

    def __str__(self):
        if self._user_matrix != []:
            symbol_count_list = []
            for num_el in range(len(self._user_matrix[0])):
                i = 0
                symbol_count = 0
                for num_elm in range(len(self._user_matrix)):
                    i = len(str(self._user_matrix[num_elm] [num_el]))
                    if i > symbol_count:
                        symbol_count = i
                symbol_count_list.append(symbol_count)

            for num_el, el in enumerate(self._user_matrix):
                for num_elm, elm in enumerate(el):
                    current_str = str(elm).ljust(symbol_count_list[num_elm])
                    print(f'{current_str}    ', end='')
                print('\n')
        return ''
    def __add__(self, other):
        if len(self._user_matrix) == len(other._user_matrix):
            res_list = [[(self._user_matrix[num_el][num_elm] + other._user_matrix[num_el][num_elm])\
                             for num_elm in range(len(self._user_matrix[num_el]))]
                         for num_el in range(len(self._user_matrix))]
            res = Matrix()
            res.matrix = res_list
            return res
        else:
            return 'Ошибка: невозможно сложить матрицы разных размеров.'

    @property
    def matrix(self):
        return self._user_matrix


    @matrix.setter
    def matrix(self, matr):
        if not isinstance(matr, list):
            print('Ошибка: matrix должен быть списком списков.')
            return

        for el in matr:
            if not isinstance(el, list):
                print('Ошибка: каждый элемент списка matrix должен быть списком.')
                return
            if len(el) != len(matr[0]):
                print('Ошибка: все вложенные списки должны быть одного размера')
                return
            for elm in el:
                if not isinstance(elm, (float, int)):
                    print('Ошибка: каждый элемент вложенного списка должен быть числом')
                    return

a = Matrix()
b = Matrix()
a.matrix = [[1, 2, 3, 4], [4.6, 5, 6, 4], [1, 1, 1, 1]]
b.matrix = [[7, 3, 1, 4], [10, 11.2, 12, 0], [2, 3, 1, 3]]
c = a + b

print(c)
