'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.'''

class ZeroDivision:
    def __init__(self, user_num1, user_num2):
        self.user_num1 = user_num1
        self.user_num2 = user_num2

    @staticmethod
    def division_by_zero(user_num1, user_num2):
        try:
            return (user_num1 / user_num2)
        except:
            return f'Делить на ноль нельзя!'

div = ZeroDivision(10, 100)
print(ZeroDivision.division_by_zero(10, 0))
print(ZeroDivision.division_by_zero(10, 0.1))
print(div.division_by_zero(100, 0))