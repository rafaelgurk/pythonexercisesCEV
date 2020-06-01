n1 = int(input('Número: ')) #Sucessor e antecessor
print('O sucessor é: {} E seu antecessor: {}'.format(n1+1, n1-1))

n2 = float(input('Número: ')) #Dobro, triplo e raizQuadrada
print('O dobro é: {}  O triplo: {}  E a raiz quadrada: {:.1f}'.format(n2*2, n2*3, pow(n2, (1/2))))

n3 = float(input('Nota 1: ')) #média Aluno
n4 = float(input('Nota 2: '))
n5 = float(input('Nota 3: '))
print('A média do aluno é: {:.2f}'.format((n3+n4+n5)/3))

n5 = float(input('Metros: ')) #Metros para Cm e Mm
print('{:.0f}m em centímetros: {:.0f}cm \nEm milímetros: {:.0f}mm'.format(n5, n5/0.01, n5/0.001))

n6 = float(input('R$')) #Real em dolar
print('Você tem: U${}'.format(n6*5.20))












