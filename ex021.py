# Identificar número primo
num = int(input(' NÚMERO -> '))
cont = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[31m', end=' ')
        cont += 1
    else:
        print('\033[34m', end=' ')
    print(i, end=' ')
if cont == 2:
    print(f'\033[m\n O NÚMERO {num} FOI DIVISÍVEL POR 1 E POR ELE MESMO\n\033[37m É UM NÚMERO PRIMO!')
else:
    print(f'\033[m\n O NUMERO {num} FOI DIVISÍVEL {cont} VEZES\n NÃO É UM NÚMERO PRIMO!')

# Identificar número primo
num = int(input('DIGITE UM NÚMERO => '))
cont = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[31m', i, end=' ')
        cont += 1
    else:
        print('\033[33m', i, end=' ')
if cont == 2:
    print('\033[m\nNúmero divisível por 1 e ele mesmo.\nÉ número primo')
else:
    print(f'\033[m\n Número divisível {cont} vezes\n Não é número primo')

# Ler idades e informar se são maiores de idade
from datetime import date
qntd = int(input('Quantas pessoas serão registradas? '))
maior = 0
menor = 0
for i in range(1, qntd+1):
    idade = int(input('Em que ano a {}º pessoa nasceu -> '.format(i)))
    if date.today().year - idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Temos {maior} pessoa(s) \033[31mmaior(es)\033[m de idade')
print(f'Temos {menor} pessoa(s)\033[33m menor(es)\033[m de idade')