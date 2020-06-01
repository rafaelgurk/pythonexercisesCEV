# Laço de repetição FOR (FOR = estrutura de repetição com variável de controle)
# Contagem regressiva com sleep 1segundo
from time import sleep
x = int(input('INÍCIO DA CONTAGEM REGRESSIVA => '))
for i in range(x, -1, -1):
    print('..{}'.format(i), end=' ')
    sleep(0.3)

# Numeros pares entre x e y
x = int(input('\nINICIO => '))
y = int(input('FIM => '))
for i in range(x, y+1):
    if x % 2 == 0:
        print(x)
    x += 1

# Soma de numeros impares multiplos de 3 entre 1 e 500
n = 0
s = 0
c = 0
for i in range(1, 500):
    if n % 2 == 1 and n % 3 == 0:
      s = s + n
      c += 1
    n += 1
print(f'A SOMA DOS {c} DÍGITOS É {s}')

