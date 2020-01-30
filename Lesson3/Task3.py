def my_func(var1: int, var2: int, var3: int) -> int:
    """
    Функция возвращает сумму двух максимальных аргументов из трех входных

    :param var1: int
    :param var2: int
    :param var3: int
    :return: int
    """
    try:
        var1 = int(var1)
        var2 = int(var2)
        var3 = int(var3)
    except ValueError:
        print('Нужно ввести целое число, а не строку!')
        return

    return sum([var1, var2, var3]) - min([var1, var2, var3])

var_1 = input('Число 1: ')
var_2 = input('Число 2: ')
var_3 = input('Число 3: ')
print(f'Сумма наибольших двух чисел: {my_func(var_1, var_2, var_3)}')
