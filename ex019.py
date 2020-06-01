# Soma de numeros pares
x = int(input('\nINÍCIO => '))
y = int(input('FIM => '))
s = 0
for i in range(x, y):
    x += 1
    if x % 2 == 0:
        s += x
print(s)

# Tabuada
c = int(input('\nTABUADA DO NÚMERO => '))
for i in range(1, 11):
    print(f'{c} x {i} = {c*i}')
