my_list = input('Введите элементы списка, отделяя их запятой и пробелом:')
my_list = my_list.split(', ')
#new_list = []
len_is_odd = len(my_list) % 2
if len_is_odd:
    last_val = my_list.pop()
for i in range(0, len(my_list)-1, 2):
    #new_list.append(my_list[i+1])
    #new_list.append(my_list[i])
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
if len_is_odd:
    my_list.append(last_val)
    #new_list.append(last_val)
print(my_list)
#print(new_list)