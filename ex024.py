# NAME AGE SEX... informar homem mais velho, mulheres menos 20 anos, media de idades.
num = int(input('Quantidade de pessoas que serão registradas => '))
oldman = 0
media = 0
menos20 = 0
print('==x==' * 10)
for i in range(1, num+1):
    print(F'xxxxxxxxxxxxx {i}º PESSOA xxxxxxxxxxxxx')
    name = str(input('SEU NOME> '))
    age = int(input('IDADE> '))
    sex = str(input('SEXO [M/F]> '))
    media += age
    if sex != 'M' and sex != 'F':
        print('--> OPÇÃO INVÁLIDA!! <--')
        exit()
    if sex == 'M' and age > oldman:
        oldman = age
        oldmanname = name
    if sex == 'F' and age < 20:
        menos20 += 1
media = media/num
print('==x==' * 10)
if oldman == 0:
    oldmanname = 'MASCULINO NÃO REGISTRADO'
    print('MEDIA ENTRE AS IDADES INFORMADAS>> {} ANOS'.format(int(media)))
    print('HOMEM MAIS VELHO>> {}'.format(oldmanname))
    print('QUANTIDADE DE MULHERES REGISTRADAS COM MENOS DE 20 ANOS>> {}'.format(menos20))
else:
    print('MEDIA ENTRE AS IDADES INFORMADAS>> {} ANOS'.format(int(media)))
    print('HOMEM MAIS VELHO>> {} COM {} ANOS DE IDADE'.format(oldmanname, oldman))
    print('QUANTIDADE DE MULHERES REGISTRADAS COM MENOS DE 20 ANOS>> {}'.format(menos20))
