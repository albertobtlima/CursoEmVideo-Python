# Exercício 075
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares

num = (int(input('Digite o 1ª número: ')), int(input('Digite 0 2ª número: ')),
       int(input('Digite o 3ª número: ')), int(input('Digite 0 4ª número: ')),)
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
