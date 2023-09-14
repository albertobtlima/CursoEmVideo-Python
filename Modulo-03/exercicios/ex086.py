# Exercício 086
# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tela, com a formatação correta.

"""
num = [[], [], []]
valor = 0
for c in range(0, 3):
    valor = int(input('Digite um valor: '))
    num[0].append(valor)
for c in range(0, 3):
    valor = int(input('Digite um valor: '))
    num[1].append(valor)
for c in range(0, 3):
    valor = int(input('Digite um valor: '))
    num[2].append(valor)
print(f'[{num[0][0]:^5}] [{num[0][1]:^5}] [{num[0][2]:^5}]')
print(f'[{num[1][0]:^5}] [{num[1][1]:^5}] [{num[1][2]:^5}]')
print(f'[{num[2][0]:^5}] [{num[2][1]:^5}] [{num[2][2]:^5}]')
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
