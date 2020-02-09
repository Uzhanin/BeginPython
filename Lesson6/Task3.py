"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
 income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
  оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
   В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
    с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
     передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    _income = {'wage': None, 'bonus': None}
    def __init__(self, name, surname, position, wage = 0, bonus = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income.update({'wage': int(wage), 'bonus': int(bonus)})

class Position(Worker):
    def get_full_name(self):
        print(' '.join([self.name, self.surname]))

    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))

# Создаем объект ivanov
ivanov = Position('Ivan', 'Ivanov', 'Vendor', 30000, 5000)

print(ivanov.name)
print(ivanov.surname)
print(ivanov.position)
ivanov.get_full_name()
ivanov.get_total_income()

#print(ivanov.income)
print(ivanov._income)


# Создаем объект irinkina
irinkina = Position('Irina', 'Irinkina', 'Manager', 25000, 3000)

print(irinkina.name)
print(irinkina.surname)
print(irinkina.position)
irinkina.get_full_name()
irinkina.get_total_income()

#print(ivanov.income)
print(irinkina._income)
