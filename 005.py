# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


from func import get_number


def get_fibbonacci_list(size=10) -> list:
    list = [0, 1]
    for i in range(2, size+1):
        list.append(list[i-1]+list[i-2])
    new_list = list[:]
    new_list.pop(0)
    for i in range(1, size, 2):
        new_list[i] *= -1
    return new_list[::-1] + list


number = get_number('Input the number -> ', 'Input\'s error. Try again -> ')
print(get_fibbonacci_list(number))