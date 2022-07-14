# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from decimal import Decimal


def get_min_fractional_part(list: list) -> float:
    min = 1
    max = 0
    for i in list:
        if min % 1 > i % 1: min = i
        if max % 1 < i % 1: max = i
    return max - min 


list = [1.1, 1.2, 3.1, 5, 10.01]
print(get_min_fractional_part(list))
