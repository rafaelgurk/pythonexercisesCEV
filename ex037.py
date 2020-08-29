# 2 - Tupla 20 primeiros colocados de campeonado.
# A) Primeiros 5 colocados
# B) Últimos 4 da tabela
# C) Lista dos times em ordem alfabética
# D) Em que posição está o ---
print('=-=-=-=-= 20 PRIMEIROS TIMES DO CAMPEONATO =-=-=-=-=')
times = 'Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Athletico-PR', 'Sao Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goias', 'Bahia', 'Vasco da Gama', 'Atletico-MG', 'Fluminense', 'Botafogo', 'Ceara', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avai'
print(times)
print('=-='*15)

# 5 primeiros colocados
print('A) Primeiros 5 colocados>> ')
for i in range(0, 5):
    print(f'{i+1}° {times[i]}')
print('=-='*15)

# 4 ultimos colocados
print('B) 4 último colocados>> ')
for i in range (16, 20):
    print(f'{i+1}° {times[i]}')
print('=-='*15)

# Ordem alfabética
print('C) Lista dos times em ordem alfabética>> ')
print(sorted(times))
print('=-='*15)

# Posição Chapecoense
print('D) Chapecoense está na {}° Posição.'.format(times.index('Chapecoense')+1))
