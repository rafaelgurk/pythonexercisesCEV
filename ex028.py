# Fibonacci sequence
fib = 0
i = 0
x = 0
aux = 1
qnt = int(input('Quantos termos -> '))
while i < qnt:
    fib += x
    x = aux
    aux = fib
    print(fib, end='.. ')
    i += 1
print('Finish', end='.')

# from math import factorial
# numb = int(input('Number to be factored>> '))
# print(factorial(numb))
numb = int(input('Number to be factored>> '))
fatorial = numb
print(f'{numb}! = ', end=' ')
if numb > 1:
    print(f'{numb} * ', end='')
    while numb > 1:
        numb -= 1
        fatorial *= numb
        print(f'{numb}', end='')
        print(' * ' if numb > 1 else ' = ', end='')
    print(fatorial)
elif numb == 0:
    print('1')
else:
    print('Only numbers >= 0 can be factored')

