# Tupla 0 a 20. Digitar um valor, escrever por extenso
tup = 'Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete',\
      'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',\
      'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte',
ext = int(input('Número a ser escrito [0/20]>> '))
while True:
    if 0 <= ext <= 20:
        break
    else:
        ext = int(input(('Número inválido, tente novamente!!\nDigite um número [0/20]>> ')))
print(tup[ext])
