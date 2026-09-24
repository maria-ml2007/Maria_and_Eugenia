#МИКРОКАЗИК
start = int(100)
bln_c = start
a = 0
b = 0
c = 0

print('Включить игру?')
print('Напишите true чтобы вкл. и false чтобы выкл.')
f = input()

while f == 'true':
    print('Сыграть?', 'Напишите да или нет')
    q = str(input())
    bln_c = int(bln_c) #  целые числа
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    print('|', a, '|', b, '|', c, '|')
    if a == b == c:
        bln_c = 2 * bln_c
        print('ПОЗДРАВЛЯЕМ! Ваш счёт удвоен! Текущий баланс', bln_c)
    elif a == b or a == c or b == c:
        bln_c == 1.5 * bln_c
        print('ПОЗДРАВЛЯЕМ! Ваш счёт вырос на 50%! Текущий баланс', bln_c)
    else:
        bln_c = 0.5 * bln_c
        print('ВЫ ПРОИГРАЛИ! Текущий баланс', bln_c)
    if q == 'да' and bln_c == 0:
        print('Недостаточно средств, пополните счёт')
    elif q == 'нет':
        print('Игра завершена')
