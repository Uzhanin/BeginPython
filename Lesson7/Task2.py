"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
 которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
  У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
 Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
 реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

"""
from abc import abstractmethod, ABC

class Clothes(ABC):
    cons = 0

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Clothes.cons += self.size / 6.5 + 0.5


    def consumption(self):
        return str(self.size / 6.5 + 0.5)



class Suit(Clothes):
    def __init__(self, heigth):
        self.heigth = heigth
        Clothes.cons += self.heigth * 2 + 0.3

    @property
    def consumption(self):
        return str(self.heigth * 2 + 0.3)

coat1 = Coat(52)
print(f'На пальто coat1 затрачено {coat1.consumption()} м ткани')

suit1 = Suit(1.9)
print(f'На костюм suit1 затрачено {suit1.consumption} м ткани')

suit2 = Suit(1.7)
print(f'На костюм suit2 затрачено {suit2.consumption} м ткани')

print(f'На все суммарно затрачено {Clothes.cons} м ткани')





