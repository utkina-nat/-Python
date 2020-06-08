''' Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.'''

class ComplexNumber:
    def __init__(self, real= None, imag=None):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return '{}{}{}i'.format(self.real, sign, self.imag)
    __repr__ = __str__


class ComplexCalc(ComplexNumber):
    def add(self, c1, c2):
        real = c1.real + c2.real
        imag = c1.imag + c2.imag
        return ComplexNumber(real, imag)

    def mul(self, c1, c2):
        real = c1.real * c2.real - c1.imag * c2.imag
        imag = c1.imag * c2.real + c1.real * c2.imag
        return ComplexNumber(real, imag)




calc = ComplexCalc()
print(calc.add(ComplexNumber(1, 2), ComplexNumber(3, 4)))
print(calc.mul(ComplexNumber(1, 2), ComplexNumber(3, 4)))



