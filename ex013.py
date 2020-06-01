#  Número random 0 a 5 - Usuário tenta adivinhar
from random import randint
num = int(randint(0, 5))
tentativa = int(input('Tente adivinhar o número pensado [0..5]: '))
if tentativa == num:
    print('VOCÊ ACERTOU!\nO número pensado foi {}'.format(num))
else:
    print('VOCÊ ERROU!\nO número pensado foi {}'.format(num))

#  Ler velocidade de um carro. Maior que 80km multa R$7.00 por km
velocidade = int(input('QUAL A VELOCIDADE: '))
if velocidade <= 80:
    print('ESTÁ TUDO BEM ENTÃO')
else:
    multa = (velocidade-80)*7
    print('MULTADOR! VALOR A PAGAR R${:.1f}'.format(multa))

#  Par ou Ímpar
n = int(input('NÚMERO: '))
if n % 2 == 1:
    print('NÚMERO {} É IMPAR'.format(n))
else:
    print('NÚMERO {} É PAR'.format(n))

#  Distância de viagem. R$0.50 por km até 200km. R$0.45 por km mais que 200
distancia = int(input('QUAL A DISTÂNCIA DA VIAGEM: '))
if distancia <= 200:
    print('TOTAL A PAGAR: R$', distancia*0.50)
else:
    print('TOTAL A PAGAR: R$', distancia*0.45)

#  Salário +R$1.250 +10%. Menores ou iguais 15%
salario = float(input('QUAL SEU SALÁRIO: '))
if salario > 1250.00:
    print('SALÁRIO COM 10% DE AUMENTO: ', salario+(salario*0.10))
else:
    print('SALÁRIO COM 15% DE AUMENTO: ', salario+(salario*0.15))




