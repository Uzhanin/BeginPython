my_list = [1, 70, 7]
el = input('Введите новый элемент: ')
while el.isdigit():
    my_list.append(int(el))
    print(sorted((my_list), reverse=True))
    el = input('Введите новый элемент: ')