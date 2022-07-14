# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from decimal import Decimal


def get_min_fractional_part(list: list) -> float:
    min = Decimal('1')
    max = Decimal('0')
    for i in list:
        float_part = Decimal(str(i%1))
        if min % 1 > float_part: min = i
        if max % 1 < float_part: max = i
    result = max - min
    return float(result.to_eng_string())


list = [1.1, 1.2, 3.1, 5, 10.01]
print(get_min_fractional_part(list))
