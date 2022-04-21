import random


def string_generator(amount, str_arr):
    for x in amount:
        random_str = ''.join(random(str_arr), x)

    print(random_str)


string_generator(2, list['a', 'b', 'c', 'd'])
