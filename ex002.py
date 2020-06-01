#Ler um número e exibir informações sobre o que foi digitado
a = input('Digite algo: ')
print(type(a))
print(a.isascii(), a.isalnum(), a.isalpha(), a.isdecimal(), a.isnumeric(), a.isupper())

n1 = float(input('Número: '))
n2 = float(input('Número: '))
div = n1/n2
print('EDIÇÃO 2 CASAS {:.2f}'.format(div))





