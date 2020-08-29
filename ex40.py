# Quatro valores A) Quantas vezes numero 9 B) Qual a posição do 3 C) Quais são pares
quantidada = int(input('Quantos números? '))
tup = tuple(int(input('Numero>> ')) for i in range(0, quantidada))


print(f'\n9 foi digitado {tup.count(9)} vezes')
if 3 in tup:
    print(f'\n3 digitado na posicao {tup.index(3)+1}')
else:
    print('\n3 não foi digitado')
print('\nPares digitados>> ', end=' ')
for c in tup:
    if c % 2 == 0:
        print(c, end=' ')
print('\n', tup)
