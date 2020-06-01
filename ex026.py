# Estrutura WHILE (WHILE = estrutura de repetição com teste lógico)
c = 0
while c != 8:
    c = int(input('digite um valor - '))
    print(c)

# Ler sexo aceitando apenas 'M' ou 'F'
i = ''
while i != 'M' and i != 'F':
    sex = str(input('SEXO>> ')).upper()
    i = sex
    if sex != 'M' and sex != 'F':
        print('Dado inválido. Por favor informe corretamente!')
print('Sexo {} registrado com sucesso'.format(sex))
