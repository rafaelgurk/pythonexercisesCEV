import math
import random

n = float(input('Digite um número fracionado: '))  # Return integer value
print(math.trunc(n))

catetoOposto = float(input('Cateto Oposto: '))  # hypotenuse of right triangle
catetoAdjacente = float(input('Cateto Adjacente: '))
print('O comprimento da hipotenusa é: {:.2f}'.format(math.hypot(catetoOposto, catetoAdjacente)))

angulo = float(input('Ângulo: '))  # Sine Cossine Tangent
print(f' Seno = {math.sin(angulo):.3f}\n Cosseno = {math.cos(angulo):.3f}\n Tangente = {math.tan(angulo):.3f}')

al1 = input('1º Aluno: ')  # Random student
al2 = input('2º Aluno: ')
al3 = input('3º Aluno: ')
al4 = input('4º Aluno: ')
print('Aluno sorteado: {}'.format(random.choice([al1, al2, al3, al4])))


