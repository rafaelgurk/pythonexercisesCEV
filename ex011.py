#  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
n = input('Digite um número de 0 a 9999: ').strip()
print(f'Unidade: {n[0:1]}\nDezena: {n[1:2]}\nCentena: {n[2:3]}\nMilhar: {n[3:4]}')

#  Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

city = str(input('Cidade -->  ')).strip()
print('Cidade começa com palavra "Santo": ', 'SANTO' in city[:5].upper())
print(city)

#  Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Seu nome completo: ').strip()
print('"Silva" em seu nome: ', 'SILVA' in nome.upper())


