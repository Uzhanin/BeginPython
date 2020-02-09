"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
   Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
     Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
      и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
 Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.ispolice = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')


class TownCar(Car):

    def classname(self):
        print('Класс TownCar')

    def show_speed(self):
        if self.speed <= 60:
            print(f'Скорость {self.speed} км/ч')
        else:
            print(f'Текущая скорость {self.speed}. Скорость больше 60 км/ч')


class SportCar(Car):

    def classname(self):
        print('Класс SportCar')


class WorkCar(Car):

    def classname(self):
        print('Класс WorkCar')

    def show_speed(self):
        if self.speed <= 40:
            print(f'Скорость {self.speed} км/ч')
        else:
            print(f'Текущая скорость {self.speed}. Скорость больше 40 км/ч')


class PoliceCar(Car):

    def classname(self):
        print('Класс PoliceCar')


car1 = Car(50, 'red', 'Volga', False)
print(car1.speed)
print(car1.color)
print(car1.name)
print(car1.ispolice)
car1.go()
car1.turn('налево')

print('*' * 30)

car2 = TownCar(70, 'yellow', 'UAZ', False)
print(car2.speed)
print(car2.color)
print(car2.name)
print(car2.ispolice)
car2.classname()
car2.go()
car2.show_speed()

print('*' * 30)

car3 = PoliceCar(110, 'white and blue', 'LADA', True)
print(car3.speed)
print(car3.color)
print(car3.name)
print(car3.ispolice)
car3.show_speed()
car3.classname()