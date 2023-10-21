# Exercício 103
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz  de mostrar a
# ficha  do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato.')


nome = str(input("Nome do jogador: "))
gol = str(input("Número de gols: "))
if nome.isnumeric():
    nome = ''
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)
