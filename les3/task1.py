'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def my_func (a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "Делить на 0 нельзя!"
    except ValueError:
        return "ВВедитее только число!"
print(my_func(int(input("Enter a = ")), int(input("Enter b = "))))