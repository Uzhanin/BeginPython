month = int(input('Введите номер месяца: '))
seasons = ['Зима', 'Весна', 'Лето', 'Осень']
if month == 12 or month < 3:
    print(seasons[0])
elif month > 2 and month < 6:
        print(seasons[1])
elif month > 5 and month < 9:
        print(seasons[2])
else:
        print(seasons[3])


dict_months = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
print(dict_months.get(month))