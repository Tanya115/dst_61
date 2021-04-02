from random import *


def game_core_v2(number):
    count = 1
    fn, fx = 1, 101
    predict = fx / 2
    while number != predict:
        count += 1

        if number > predict:
            fn = predict + 1

        elif number < predict:
            fx = predict - 1

        predict = (fx + fn) / 2

    return count # выход из цикла, если угадали


num = randint(1, 101)
print(num)
print(game_core_v2(num))


