def my_div(var_1: float, var_2: float) -> float:
    """
    Возвращает результат деления одного числа на другое число

    :param var_1: float
    :param var_2: float
    :return: float
    """
    try:
        var_1 = float(var_1)
        var_2 = float(var_2)
        result = var_1 / var_2
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        return
    except ValueError:
        print('Нужно ввести число, а не строку!')
        return

    return result

var_1 = input('Введите делимое: ')
var_2 = input('Введите делитель: ')
print(my_div(var_1, var_2))