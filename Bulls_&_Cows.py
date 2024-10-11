'''
Быки и коровы – логическая игра для двоих игроков.

Правила игры:
По правилам игры, компьютер случайным образом выбирает
четырёхзначное число таким образом,
чтобы первой значащей цифрой не был 0 и чтобы все цифры,
составляющие это число были бы уникальными.

Если в предложенном вами числе несколько цифр
оказались на своём месте, компьютер сообщает
сколько есть таких цифр.

Цифра на своём месте называется БЫКОМ.
Если в предложенном вами числе несколько цифр
оказались не на своём месте, компьютер сообщает
сколько есть таких цифр.
Цифра не на своём месте называется КОРОВОЙ.
'''
from random import choice


def random_number(x):
    # создаём случайное число от 1023 до 9876, где все цифры уникальны
    posled = '0123456789'
    num = choice(posled[1:10])
    for i in range(3):
        posled = ''.join(posled.split(num[i]))
        num += choice(posled)
    return num


c_num = random_number(0)

moves = 0
while True:
    p_num = input('Введите число: ')

    if len(p_num) == 4 and len(set(p_num)) == 4:  # проверка
        moves += 1
        bulls = 0
        cows = 0
        for i in range(4):
            if p_num[i] == c_num[i]:
                bulls += 1
            elif p_num[i] in c_num:
                cows += 1

        if bulls >= 1:
            bulls_word = 'быка'
        else:
            bulls_word = 'быков'

        if cows == 0:
            cows_word = 'коров'
        elif cows == 1:
            cows_word = 'корову'
        else:
            cows_word = 'коровы'

        result = f'Число {p_num} содержит {bulls} {bulls_word} 🐂 и {cows} {cows_word} 🐄'
        print(result)

        if bulls == 4:
            print('------------------------------------------')
            print('Вы отгадали число', c_num, 'за', moves, 'ходов')
            break

    else:
        print('❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌\nВведите число по правилам игры!')