"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

"""
my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('file_for_task4.txt', 'r') as file_in:
    with open('file_for_task4_out.txt', 'w') as file_out:
        for line in file_in:
            line = line.split(' ')
            for key in my_dict:
                if key == line[0]:
                    line[0] = my_dict.get(key)
                    rus_line = ' '.join(line)
                    file_out.write(rus_line)
