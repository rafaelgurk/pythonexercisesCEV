#  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper()
print('Letra "A" aparece {} vezes '.format(frase.count('A')))
print('A letra "A" aparece primeiro na posição -> {}\nÚltima posição letra "A" -> {}'.format(frase.find('A')+1, frase.rfind('A')+1))

#  Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Seu nome completo: ')).split()
print('Primeiro nome: {}\nÚltimo nome: {}'.format(nome[0], (nome[-1])))
