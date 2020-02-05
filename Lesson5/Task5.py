"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


"""
import random

rand_list = []
# Генерируем 10 случайных целых чисел из диапазона от -100 до 100 и пишем в файл
with open('file_for_task5.txt', 'w') as file_out:
    for num in range(10):
        rand_list.append(str(random.randint(-100, 100)))
        my_str = ' '.join(rand_list)
    file_out.write(my_str)

# Читаем из файла и считаем суммму
with open('file_for_task5.txt', 'r') as file_in:
    true_num = []
    for line in file_in:
        numbers = line.split(' ')
        for num in numbers:
            true_num.append(int(num))
    print(f'Были сгенерированы числа: {true_num}')
    print(f'Сумма всех чисел: {sum(true_num)}')
