# Tupla produtos e preços montar lista de preços
produtos = ('arroz', '5.99',
       'feijao', '3.99',
       'carne', '12.99')

print('-'*39)
print(f'{"LISTAGEM":^40}')
print('-'*39)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i].upper():.<30}', end=' ')
    else:
        print(f'R${produtos[i]:>7}')
print('-'*39)
