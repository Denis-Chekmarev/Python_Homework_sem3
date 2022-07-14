from random import randint as rand


def get_number(text: str, error_text = 'Wrong input. Try again -> ') -> int:
    print(text, end='')
    while True:
        numb = input()
        if numb.isdigit():
            numb = int(numb)
            return numb
        else:
            print(error_text, end='')


def get_random_list(size: int, min=-100, max=101) -> list:
    list_number = []
    for i in range(size):
        list_number.append(rand(min, max))
    return list_number


def get_fractional_part(number: float) -> int:
    try:
        return int(str(number).split('.')[1])
    except ValueError:
        return 0