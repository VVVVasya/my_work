import random
def get_exit():
    numbers = list(range(3, 21))
    n = random.choice(numbers)
    pair_num_1 = list(range(1, n))
    pair_num_2 = list(range(1, n))
    result = ''

    for i in pair_num_1:
        for j in pair_num_2:
            if i <= j and n % (i + j) == 0:
                result = result + str(i) + str(j)
    print('Первое число:', n)
    print('Второе число для вставки:', result, ' - пароль')

get_exit()