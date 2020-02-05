"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

"""
with open('file_for_task2.txt', 'r') as file_in:
    print('Номер строки --- количество слов')
    str_count = 0
    for line in file_in:
        str_count += 1
        line = line.split(' ')
        # количества будут выведены в виде: номер строки --- количество слов
        print(str_count, '---', len(line))
    print(f'Количество строк в файле: {str_count}')