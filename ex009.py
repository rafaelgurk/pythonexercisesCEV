texto = str(input('Digite: '))
print(texto[2::2])

print(texto.replace(texto, 'texto trocado'))  # troca texto pelo indicado
print(texto.upper())  # Tudo em letras maiúsculas
print(texto.lower())  # Todas em minúsculas
print(texto.title())  # Cada palavra com letra maiúscula
print(texto.capitalize())  # Primeira letra maiúscula
print(texto.strip())  # Retira espaços inúteis fim e começo de frase
print(texto.split())  # Divisão de strings
print(texto.split(maxsplit=0))  # Delimita a divisão
print('-'.join(texto))  # Adiciona '' na frase digitada

texto2 = str(input('Digite: '))
print(texto2.find('abcd'))  # Encontrar o que for pedido ''
print('abcd' in texto2)





