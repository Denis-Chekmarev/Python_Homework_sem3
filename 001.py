# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from func import get_random_list


def get_sum_odd_indexs(list: list) -> int:
    sum = 0
    for i in range(0, len(list), 2):
        sum += list[i]
    return sum 


if __name__=='__main__':
    origin_list = get_random_list(5, -10, 10)
    print(origin_list)
    print(get_sum_odd_indexs(origin_list))