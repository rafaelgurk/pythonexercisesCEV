# Valor total gasto , produtos 1000+, produto mais barato
i = total = more1000 = 0
while True:
    i += 1
    product = str(input('Produto>> '))
    value = int(input('Valor>> R$'))
    print('=-='*15)
    total += value
    if i == 1:
        cheap = value
        cheaper = product
    if value < cheap:
        cheap = value
        cheaper = product
    if value > 1000:
        more1000 += 1
    cnt = str(input('Coninue [Y/N]>> ')).upper()
    print('=-='*15)
    if cnt != 'Y':
        break
print(f'Total gasto>> R${total}')
print(f'Produtos com valor maior de R$1000.00>> {more1000}')
print(f'Produto mais barato {cheaper} no valor de R${cheap}')