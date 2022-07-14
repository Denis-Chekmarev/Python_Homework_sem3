# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from func import get_random_list


def get_mult_list(list: list) -> list:
    new_list = []
    lengh = len(list)
    for i in range(int(len(list)/2+1)):
        multiplication = list[i] * list[len(list) - i-1]
        new_list.append(multiplication)
    return new_list


origin_list = get_random_list(5, 1, 11)
print(origin_list)
print(get_mult_list(origin_list))
