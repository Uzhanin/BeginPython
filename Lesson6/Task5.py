"""
Реализовать класс Stationery (канцелярская принадлежность).
 Определить в нем атрибут title (название) и метод draw (отрисовка).
  Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
   Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
    Для каждого из классов метод должен выводить уникальное сообщение.
     Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка из класса Pen')

class Pencil(Stationery):
    def draw(self):
        print('Отрисовка из класса Pencil')

class Handle(Stationery):
    def draw(self):
        print('Отрисовка из класса Handle')

thing_1 = Stationery('Перо')
print(thing_1.title)
thing_1.draw()
print('*' * 30)

thing_2 = Pen('Ручка')
print(thing_2.title)
thing_2.draw()
print('*' * 30)

thing_3 = Pencil('Карандашик')
print(thing_3.title)
thing_3.draw()
print('*' * 30)

thing_4 = Handle('Маркер')
print(thing_4.title)
thing_4.draw()
print('*' * 30)
