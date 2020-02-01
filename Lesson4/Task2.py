"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

"""
import random

print('Введите границы списка')
min_val = int(input('Минимальное число: '))
max_val = int(input('Максимальное число: '))
quantity = int(input('Количество элементов: '))

# Генерируем последовательнсть чисел
sequence = [el for el in range(min_val, max_val)]
# Перемешиваем
random.shuffle(sequence)
# Отбираем нужное количество
random_list = sequence[:quantity]


# Делаем выборку в соответствии с уловием задачи
result_list = []
i = 0
for i in range(1, len(random_list), 1):
    if random_list[i] > random_list[i-1]:
        result_list.append(random_list[i])
print(f'Исходный список: {random_list}')
print(f'Результат: {result_list}')






