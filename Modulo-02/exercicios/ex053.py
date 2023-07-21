# Exercício 053
# Crie um programa que leia uma frase qualquer e giga se ela é um Palíndromo,
# desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

'''inverso = ''
    for letra in range(len(junto) - 1, - 1, -1):
        inverso += junto[letra]'''

print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')
