my_dict = {'Vasya': 1199, 'Petya': 1583, 'Dasha': 1828}
print(my_dict)
print(my_dict['Petya'])
print(my_dict.get('Svetya', 'Такого ключа нет'))
my_dict.update({'Stalyn': 1878, 'Munhgausen': 1720})
a = my_dict.pop('Vasya')
print(a)
print(my_dict)
my_set = {'Vasya', 1.1, 358, True, 'Vasya'}
print(my_set)
my_set.update({False, 'X'})
my_set.remove(True)
print(my_set)