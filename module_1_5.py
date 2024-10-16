immutable_var =  3, "Вася", True
print(immutable_var)
#immutable_var[0] = 5
#print(immutable_var)
#Тип ошибки сообщает, что кортеж не поддерживает обращение по элементам
mutable_list = [ 3, "Вася", True]
mutable_list[1:] = 5, "Петя"
print(mutable_list)
