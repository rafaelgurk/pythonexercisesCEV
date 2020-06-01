# Detectar PALÍNDROMO
string = str(input('Digite aqui>> '))
frase = string
string = string.upper().replace(' ', '')
if string == string[::-1]:
    print(f'A frase>> {frase}\nInvertida>> {frase[::-1]}\nÉ PALÍNDRAMO!')
else:
    print(f'A frase>> {frase}\nInvertida>> {frase[::-1]}\nNÃO É PALÍNDRAMO!')
