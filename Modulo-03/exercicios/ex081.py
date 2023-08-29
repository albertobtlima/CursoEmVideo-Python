# Exercício 081
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# a) quantos números foram digitados.
# b) a lisrta de valores, ordenada de forma decrescente.
# c) se o valor 5 foi digitado e está ou não na lista.

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
    if resp not in 'SN':
        print('Digite novamente!')
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da ista!')
else:
    print('O valor 5 não foi encontrado na lista!')
