#  dec2any
numero = int(input('DIGITE O NÚMERO A SER CONVERTIDO => '))
print('===============OPÇÕES===============')
print('[ 1 ] BINÁRIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL')
base = int(input('SUA ESCOLHA => '))
print('====================================')
if 1 == base:
    print(f'NUMERO {numero} EM BINÁRIO = {bin(numero)[2:]}')
elif 2 == base:
    print(f'NUMERO {numero} EM OCTAL = {oct(numero)[2:]}')
elif 3 == base:
    print(f'NUMERO {numero} EM HEXADECIMAL = {hex(numero)[2:]}')
else:
    print('OPÇÃO INVÁLIDA')