# Exercício 082
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
# Extras que vão conter apenas os vaslores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
    if resp not in 'NS':
        print('Erro! Escolha novamente.')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
