"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

"""

out_f = open('file_for_task1.txt', 'w')
while True:
    new_str = input('Новая строка: ')
    if not new_str == '':
        out_f.write(new_str + '\n')
    else:
        break
out_f.close()