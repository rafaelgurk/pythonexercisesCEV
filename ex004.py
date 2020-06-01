b = float(input('Largura da parede: ')) #Qntd Tinta para Area total
a = float(input('Altura da parede: '))
print('A área é: {}m², e você utilizará {} litros de tinta'.format(b*a, (b*a)/2))

pr = float(input('Preço: R$')) #Desconto 5%
dct = pr - (pr*(5/100))
print('Valor R${:.2f} com desconto de 5% --> R${:.2f}'.format(pr, dct))

slr = float(input('Salário: ')) #15% de aumento
nvslr = slr + (slr*15/100)
print('Salário de R${:.2f} com 15% de aumento é R${:.2f}'.format(slr, nvslr))

C = float(input('Temperatura em Celsius: ')) #ºC para ºF
F = C*1.8+32
print('{}ºC = {}ºF'.format(C, F))

d = int(input('Quantos dias com o carro: ')) #0.15 por KM - 60 por dia
km = float(input('Quantos KM foram rodados? '))
valor = (km*0.15) + (d*60)
print('Total a pagar: R${:.2f}'.format(valor))





