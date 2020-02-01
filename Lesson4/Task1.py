"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

def salary(hours, rate, bonus):
    """
    Функция вычисляет зарплату по формуле: (выработка в часах*ставка в час) + премия
    :param hours:
    :param rate:
    :param bonus:
    :return:
    """
    try:
        hours = float(hours)
        rate = float(rate)
        bonus = float()
        return hours * rate + bonus
    except ValueError:
        print('Введены не числа')
        return

from sys import argv

filename, hours, rate, bonus = argv
my_salary = salary(hours, rate, bonus)
print(f'Зарплата составила: {my_salary} р.')
