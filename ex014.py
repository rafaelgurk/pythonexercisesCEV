#  Ano bissexto
ano = int(input('ANO: '))
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('ANO BISSEXTO!')
else:
    print('ANO NÃO É BISSEXTO')

#  Ler 3 número, informar maior e menor
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))
numeros = [n1, n2, n3]

print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor número digitado foi {}'.format(min(numeros)))

#  Ler 3 retas e informar se podem formar um triângulo
reta1 = float(input('RETA 1 > '))
reta2 = float(input('RETA 2 > '))
reta3 = float(input('RETA 3 > '))
lista = sorted([reta1, reta2, reta3])
if (lista[0]+lista[1] >= lista[2]) and (lista[0] + lista[2] >= lista[1]):
    print('FORMA TRIÂNGULO')
else:
    print('NÃO FORMA TRIÂNGULO')
