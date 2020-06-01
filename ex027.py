# Menu opções [1]soma [2]multiplica [3]maior [4]novos valores [5]finaliza
num1 = float(input('1º Número> '))
num2 = float(input('2º Número> '))
i = 0
maior = 0
while i != 5:
    print('=-='*15)
    print('''OPÇÕES
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR VALOR
[4] NOVOS VALORES
[5] FINALIZAR PROCESSO
''')
    opt = int(input('--> '))
    print('=-='*15)
    i = opt
    if 5 >= opt > 0:
        if opt == 1:
            print(f'A soma entre os valores {num1} e {num2} = {num1+num2}')
        if opt == 2:
            print(f'A multiplicação entre {num1} e {num2} = {num1*num2}')
        if opt == 3:
            if num1 > num2:
                maior = num1
                print(f'Entre {num1} e {num2} >> Maior {maior}')
            elif num1 < num2:
                maior = num2
                print(f'Entre {num1} e {num2} >> Maior {maior}')
            else:
                print(f'Os valores {num1} e {num2} são iguais')
        if opt == 4:
            print('--- NOVOS VALORES ---')
            num1 = float(input('1º Número> '))
            num2 = float(input('2º Número> '))
    else:
        print('Dado inválido. Por favor tente novamente.')
print('Finalizando...')
