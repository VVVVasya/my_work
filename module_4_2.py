# Домашнее задание по уроку "Пространство имен"
#
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# 1. Создайте новую функцию test_function
# 2. Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать значение "Я в области видимости функции test_function"
# 3. Вызовите функцию inner_function внутри функции test_function
# 4/ Попробуйте вызововывать inner_function вне функции test_function и посмотрите на результат выполнения программы

def test_function(): #1
    def inner_function(): #2
        print("Я в области видимости функции test_function") #2
    inner_function() #3
test_function() #4 Результат в консоли: Я в области видимости функции test_function