# Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.
nome = str(input('SEU NOME COMPLETO OU FRASE: ')).strip()
print('Frase em letras maiúsculas: ', nome.upper())
print('Frase em letras minúsculas: ', nome.lower())
splitt = nome.split()
print(f'Primeira palavra contém {len(splitt[0])} caracteres.')
print('Frase contém {} caracteres ao total'.format(len(''.join(splitt))))


