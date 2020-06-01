# 2/ par ou ímpar. Digitar 1num pc manda outro, somar os2
from random import randint
numb = int(input('Escolha um número:> '))
poui = str(input('Par ou Ímpar [P/I]:> ')).upper()
som = 0
maq = randint(1, 10)
while True:
    som = numb + maq
    print(f'Você escolheu {numb}. Máquina {maq}. Soma {som}')
    if poui == 'P':
        if som % 2 == 0:
            print(f'Você venceu {som} é PAR. Parabéns!')
            break
        print(f'{som} é ÍMPAR\nVamos tentar de novo')
        numb = int(input('Novo valor:> '))
        poui = str(input('Par ou Ímpar [P/I]:> ')).upper()
        maq = randint(1, 10)
    elif poui == 'I':
        if som % 2 == 1:
            print(f'Você venceu {som} é ÍMPAR. Parabéns!')
            break
        print(f'{som} é PAR\nVamos tentar de novo')
        numb = int(input('Novo valor:> '))
        poui = str(input('Par ou Ímpar [P/I]:> ')).upper()
        maq = randint(1, 10)
