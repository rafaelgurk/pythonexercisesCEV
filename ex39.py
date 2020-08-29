# Tupla 5 numeros aleatorios. Exibir numeros, maior e menor deles.
from random import randint

bigger = smaller = 0

for i in range(0, 5):
    x = randint(0, 99)
    if i == 0:
        bigger = x
        smaller = x
    if x > bigger:
        bigger = x
    if x < smaller:
        smaller = x
    number = x
    print(number, end='.. ')

print(f'\nMAIOR>> {bigger}')
print(f'MENOR>> {smaller}')
