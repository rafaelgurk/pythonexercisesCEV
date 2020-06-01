# 3/ cadastro de pessoas. Pessoas 18+ Quantos homens Mulheres 20-
adult = woman = men = 0
while True:
    age = int(input('Your age>> '))
    sex = str(input('Sex [M/F]>> ')).upper()
    print('=-='*15)
    if age >= 18:
        adult += 1
    if sex == 'M':
        men += 1
    if sex == 'F' and age < 20:
        woman += 1
    cnt = str(input('Continuar? ')).upper()
    print('=-=' * 15)
    if cnt == 'N':
        break
print('=-='*15)
print(f'Maiores de idade>> {adult}')
print(f'Quantidade de homens>> {men}')
print(f'Mulheres com menos de 20 anos>> {woman}')
