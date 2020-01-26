sentence = input('Введите предложение: ')
sentence = sentence.split(' ')
for idx, word in enumerate(sentence, 1):
    print(idx, word[:10])