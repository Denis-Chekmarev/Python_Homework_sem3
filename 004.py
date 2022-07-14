# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


from func import get_number


def get_binary_numb(numb: int) -> str:
    result = ''
    while numb >= 1:
        result += str(numb%2)
        numb //= 2
    return result[::-1]


number = get_number('Input the number -> ', 'Please input the number -> ')
print(get_binary_numb(number))
