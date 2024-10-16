# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)

data_structure = [

[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(*args):
    sum_ = 0
    for item in args:
        if isinstance(item, int):
            sum_ += item
        elif isinstance(item, str):
            sum_ += len(item)
        elif isinstance(item, (list, tuple, set)):
            sum_ += calculate_structure_sum(*item)
        elif isinstance(item, dict):
            sum_ += calculate_structure_sum(*item.keys(), *item.values())

    return sum_


result = calculate_structure_sum(data_structure)
print(result)

