def my_func(a: float, b: int) -> float:
    """
    Функция возводит a в степень b.
    a - действительное положительное число
    b - целое отрицательное число
    :param a: float
    :param b: int
    :return: float
    """
    try:
        a = float(a)
        b = int(b)
    except ValueError:
        print('Либо вы ввели строку, либо показатель степени не целый отрицательный')
        return
    except TypeError:
        print('Чило должно быть действительным, а не комплексным!')
        return
    if a > 0 and b < 0:
        result = 1
        for i in range(-b):
            result = result / a
        return result
    else:
        print('Число, которое необходимо возвести в степень, должно быть вещественным положительным')
        print('Показатель степени должен быть целым отрицательным числом')

num1 = input('Что будем возводить в степень: ')
num2 = input('В какую степень будем возводить: ')
print(f'Результат: {my_func(num1, num2)}')