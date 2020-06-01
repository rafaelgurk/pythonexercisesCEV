# Registrar ano de nascimento e informar maior ou menor idade
from datetime import date
qntd = int(input('Quantas pessoas serão registradas => '))
maior = 0
menor = 0
for i in range(1, qntd+1):
    ano = int(input(f'Ano de nascimento da {i}º pessoa -> '))
    if date.today().year - ano >= 21:
        maior += 1
    else:
        menor += 1
print('Registradas {} pessoa(s)\033[31m maior(es)\033[m de idade!'.format(maior))
print('Registradas {} pessoa(s)\033[32m menor(es)\033[m de idade!'.format(menor))