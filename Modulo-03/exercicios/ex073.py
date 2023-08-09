# Exercício 073
# Crie uma TUPLA preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, no ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros.                     c) Times em ordem alfanetica
# b) Os últimos 4 colocados.             d) Em que posição está o Corinthians

times = ('Botafogo', 'Flamengo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Grêmio', 'Athletico-PR', 'Cuiabá',
         'São Paulo', 'Athletico-MG', 'Cruzeiro', 'Internacional', 'Fortaleza', 'Corinthians', 'Goiás',
         'Bahia', 'Santos', 'Coritiba', 'Vasco da Gama', 'América-MG')
#print(f'Lista de times: {times}')
print('Lista de times:')
for t in times:
    print(t)
print('-=' * 10)
print('Os 5 primeiros são:')
for t in times[0:5]:
    print(t)
print('-=' * 10)
print('Os 4 últimos colocados são:')
for t in times[-4:]:
    print(t)
print('-=' * 10)
print('Times em ordem alfabética:')
for t in sorted(times):
    print(t)
print('-=' * 10)
print(f'O Corinthians esta na {times.index("Corinthians")+1} posição')
