# Tabuada contínua
numb = int(input('Tábuada do número:> '))
cont = 1
while True:
    print(f'{numb} * {cont} = {numb*cont}')
    cont += 1
    if cont == 11:
        print('=-='*15)
        numb = int(input('Novo número [Negativo para sair]:> '))
        print('=-='*15)
        if numb < 0:
            print('FIM... Obrigado!')
            break
        cont = 1

# P.A 10 primerios termos utilizando WHILE
# P.A continuar mostrando até digitar 0
first = int(input('Primeiro termo:> '))
razao = int(input('Razao:> '))
c = 10
numb = 0
print('=-=' * 15)
while c > 0:
    print(first, end='.. ')
    first += razao
    c -= 1
    numb += 1
    if c == 0:
        print('')
        print('=-=' * 15)
        c = int(input('Mais termos:> '))
print(f'Total de termos exibidos:> {numb}')
