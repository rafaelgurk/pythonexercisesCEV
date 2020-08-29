# Tupla com várias palavras e exibir as palavras que possuem vogais, e separar vogais
tupla = ('programador', 'lasarento', 'dificil', 'tentativa', 'curso', 'computador', 'caderno')

for i in tupla:
    print('\nPalavra>> {} vogal '.format(i.upper()), end='')
    for letra in i:
        if letra in 'aeiou':
            print(f' {letra}', end=' ')
