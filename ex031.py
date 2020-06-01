# FLAG = 999. Ler n numeros, informar quantos foram digitados e a soma entre eles. Desconsiderar flag
numb = 0
soma = 0
while numb != 999:
    numb = float(input('Digite um valor [999 para sair]>> '))
    if numb != 999:
        soma += numb
print(f'A soma entre os valores = {soma}')

# Ler n numeros informar MENOR e MAIOR, e a média entre eles.
n = ''
media = 0
list = []
qnt = 0
while n != 0:
    n = float(input('Number [0 to exit]:> '))
    if n != 0:
        media += n
        qnt += 1
        list += [n]
media /= qnt
print(f'Média entre os números digitados:> {int(media)}')
print(f'Maior número informado:> {max(list)}')
print(f'Menor número informado:> {min(list)}')
