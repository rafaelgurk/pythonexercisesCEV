# 5/ Banco qual valor irá sacar. Informar cédulas necessárias, tendo R$50 R$20 R$10 e R$1
vlr = float(input('Valor que deseja sacar>> R$'))
nts50 = vlr // 50
vlr %= 50
nts20 = vlr // 20
vlr %= 20
nts10 = vlr // 10
vlr %= 10
nts1 = vlr // 1
print(f'{nts50} notas de R$50.00')
print(f'{nts20} notas de R$20.00')
print(f'{nts10} notas de R$10.00')
print(f'{nts1} notas de R$1.00')


################ outra solução (copiada) #########################
valor = int(input('VALOR SAQUE> '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

