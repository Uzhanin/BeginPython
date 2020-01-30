def int_func(word: str) -> str:
    """
    Функция делает первую букву слова заглавной.
    Функция работает только со словами из малых букв латинского алфавита.
    :param word: str
    :return: str
    """
    for el in word:
        if ord(el) >= 97 and ord(el) <= 122:
            continue
        else:
            print('Не выполнены требования ко входным данным')
            break
            return
    word = word.title()
    return word

# Тестовая строка

my_string = 'tHe united kingdom'
my_string = my_string.split(' ')
new_string = ' '.join(list(map(int_func, my_string)))
print(new_string)