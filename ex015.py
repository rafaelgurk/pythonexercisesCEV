#  if elif else #
#  Ler dois números informar qual é maior, ou iguais
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('Número {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('Número {} é maior que {}'.format(n2, n1))
else:
    print('Os valores {} e {} são iguais!'.format(n1, n2))

#  Média Reprovado Aprovado Recuperação
nota1 = float(input('1º NOTA: '))
nota2 = float(input('2º NOTA: '))
nota3 = float(input('3º NOTA: '))
nota4 = float(input('4º NOTA: '))
media = (nota1+nota2+nota3+nota4)/4
if media < 4:
    print('NOTA {} = REPROVADO!'.format(media))
elif media <= 7:
    print('NOTA {} = RECUPERAÇÃO!'.format(media))
else:
    print('NOTA {} = APROVADO!'.format(media))

#  Idade = ate9-MIRIM -> 14-INFANTIL -> 19-JUNIOR -> 20-SENIOR -> +Master
idade = int(input('SUA IDADE: '))
if idade < 9:
    print('MIRIM!')
elif idade < 14:
    print('INFANTIL!')
elif idade < 19:
    print('JUNIOR!')
elif idade == 20:
    print('SENIOR!')
else:
    print('MASTER!')

#  Pagamento: dinheiro/cheque a vista 10% desconto | Cartão a vista 5% desconto | 2x preço normal | 3x no cartão 20% juros
valor = float(input('VALOR DO PRODUTO: '))
pgm = int(input('''
[1] => À VISTA DINHEIRO/CHEQUE
[2] => À VISTA CARTÃO
[3] => 2X CARTÃO
[4] => 3X CARTÃO
'''))
if pgm == 1:
    print(f'PRODUTO DE VALOR R${valor} COM 10% DE DESCONTO = R${valor-(valor*0.1)}')
elif pgm == 2:
    print(f'PRODUTO DE VALOR R${valor} COM 5% DE DESCONTO = R${valor-(valor*0.05)}')
elif pgm == 3:
    print(f'PRODUTO EM 2X CARTÃO NÃO RECEBE ALTERAÇÃO = R${valor}')
else:
    print(f'PRODUTO DE VALOR R${valor} COM 20% DE JUROS = R${valor+(valor*0.2)}')

#  Triangulo equilatero, isosceles, escaleno
r1 = float(input('RETA 1 > '))
r2 = float(input('RETA 2 > '))
r3 = float(input('RETA 3 > '))
lista = sorted([r1, r2, r3])
if (lista[0]+lista[1] >= lista[2]) and (lista[0] + lista[2] >= lista[1]):
    print('FORMA TRIÂNGULO')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES!')
    else:
        print('ESCALENO')
else:
    print('NÃO FORMA TRIÂNGULO')