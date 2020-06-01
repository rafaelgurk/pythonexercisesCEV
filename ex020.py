# Mostrar 10 termos de uma P.A (1º termo e razão)
from time import sleep
termo1 = int(input('PRIMEIRO TERMO => '))
razao = int(input('RAZÃO => '))
for i in range(1, 11):
    print(termo1, end='.. ')
    sleep(0.3)
    termo1 = termo1 + razao