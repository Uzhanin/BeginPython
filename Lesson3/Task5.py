"""
Программа подсчитывает сумму всех введенных чисел, пока не будет введно q
"""
my_sum = 0
flag = 0
while flag != 1:
    my_str = input('Введите числа, которые нужно добавить к сумме, через пробел. Либо введите q для выхода: ')
    my_str = my_str.split(' ')
    for el in my_str:
        if el == 'q':
            flag = 1
            break
        else:
            if el.isdigit():
                my_sum += int(el)
    print(f'Накопленный итог: {my_sum}')
print('Работа программы завершена')

