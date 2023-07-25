# Exercício 059
# Crie um programa que leia dois valores e mostre um menu como abaixo:
# Seu programa deverá realizar a operação solicitada em cada caso.
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos valores
# [5] sair do programa

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[1] somar
    [2] multiplicar
    [3] maior
    [4] novos valores
    [5] sair do programa''')
    opcao = str(input('Qual é a sua opção? '))
print('FIm do programa! Volte sempre!')
