# Ler nome, idade e sexo. Informar média de idade, homem mais velho, mulheres com menos 20 anos
num = int(input('Quantidade de pessoas que serão registradas> '))
media = 0
maisvelho = 0
menos20 = 0
print('==x=='*10)
for i in range(1, num+1):
    print('============== {}º PESSOA =============='.format(i))
    name = str(input('NAME => '))
    age = int(input('IDADE => '))
    sex = str(input('SEXO [M/F] >> '))
    media += age
    if sex != 'M' and sex != 'F':
        print('\n--->OPÇÃO INVÁLIDA!!<---')
        exit()
    if sex == 'M' and age > maisvelho:
        maisvelho = age
        nomehomem = name
    if sex == 'F' and age < 20:
        menos20 += 1
media = media/num
print('==x=='*10)
print('A MÉDIA ENTRE AS IDADES DIGITADAS>> {:.2f}'.format(media))
print('HOMEM MAIS VELHO>> {} COM {} ANOS DE IDADE'.format(nomehomem, maisvelho))
print('QUANTIDADE DE MULHERES COM MENOS DE 20 ANOS>> {}'.format(menos20))

# Informar maior e menor peso lido
qntd = int(input('Quantidade de medidas à registrar > '))
peso = []
for i in range(1, qntd+1):
    list = float(input(f'Peso {i}º pessoa: '))
    peso += [list]
print('Maior peso registrado: \033[34m{}Kg'.format(max(peso)))
print('\033[mMenor peso registrado: \033[34m{}Kg'.format(min(peso)))
