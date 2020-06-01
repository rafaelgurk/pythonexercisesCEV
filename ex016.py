#  Ler valor da casa, saláio e quantos anos pra pagar. Valor da parcela não pode exceder 30% do salário
casa = float(input('VALOR DA CASA: '))
salario = float(input('SEU SALÁRIO: '))
parcelas = int(input('FINANCIAR EM QUANTOS ANOS? '))
mensal = casa/(parcelas*12)
if mensal > (salario*0.3):
    print('A PARCELA MENSAL DE UMA CASA DE R${:.2f} FICARÁ EM R${:.2f}\nEMPRÉSTIMO NEGADO'.format(casa, mensal))
else:
    print('A PRESTAÇÃO MENSAL FICARÁ EM R${:.2f} POR 7 ANOS\nFINANCIAMENTO APROVADO!'.format(mensal))

#  Ler idade de um jovem informar quanto tempo falta para se alistar ou se já deveria ter
idade = int(input('IDADE: '))
if idade < 0:
    print('ESPERE NASCER PARA FAZER O CÁLCULO!! ')
elif idade < 18:
    idade = 18 - idade
    print('AINDA TEM TEMPO, FALTAM {} ANO(S) PARA OBRIGAÇÃO DE ALISTAMENTO'.format(idade))
elif idade == 18:
    print('COM {} ANOS, VOCÊ DEVE SE ALISTAR AGORA!'.format(idade))
else:
    print('VOCÊ JÁ DEVERIA TER SER ALISTADO A {} ANO(S)'.format(idade - 18))

#  IMC
peso = int(input('PESO: '))
altura = float(input('ALTURA: '))
imc = peso/(altura**2)
print('{:.1f}'.format(imc))
if imc <= 18.4:
    print('IMC {:.1f} ESTÁ ABAIXO DO PESO!'.format(imc))
elif 18.5 <= imc <= 24.9:
    print('IMC {:.1f} ESTÁ NO PESO IDEAL!'.format(imc))
elif 25 <= imc <= 29.9:
    print('IMC {:.1f} ESTÁ COM SOBREPESO'.format(imc))
elif 30 <= imc <= 34.9:
    print('IMC {:.1f} CONFIGURA OBESIDADE GRAU I')
elif 35 <= imc <= 39.9:
    print('IMC {:.1f} CONFIGURA OBESIDADE GRAU II'.format(imc))
else:
    print('IMC {:.1f} CONFIGURA OBESIDADE MÓRBIDA!!'.format(imc))
