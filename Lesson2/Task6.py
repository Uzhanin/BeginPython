i = 0
prod = {'Название': None, 'Цена': None, 'Количество': None, 'ед': None}
prod_list = []
choice = input('Хотите добавить новый товар? Да/Нет: ')
while choice == 'Да':
    i += 1
    prod['Название'] = input('Введите название: ')
    prod['Цена'] = int(input('Введите цену: '))
    prod['Количество'] = int(input('Введите количество: '))
    prod['ед'] = (input('Введите единицу измерения: '))
    prod_list.append((i, prod.copy()))
    choice = input('Хотите добавить новый товар? Да/Нет: ')

print('Список товаров: ')
for el in prod_list:
    print(el)

print('*' * 30)


anl_list = {}
names = []
prices = []
quant = []
unit = []
for el in prod_list:
    names.append(el[1].get('Название'))
    prices.append(el[1].get('Цена'))
    quant.append(el[1].get('Количество'))
    unit.append(el[1].get('ед'))
anl_list['название'] = set(names)
anl_list['цена'] = set(prices)
anl_list['количество'] = set(quant)
anl_list['ед'] = set(unit)


print('Аналитика: ')
for el in anl_list.items():
    print(el)

