# Exercício 068
# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o
# jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vit = 0
print('-' * 30)
print('JOGO PAR OU IMPAR')
print('-' * 30)
while True:
    jog = int(input('Digite um número: '))
    com = randint(0, 10)
    total = jog + com
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador jogou {com}. Total de {total}, ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vit += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vit += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vit} vezes.')
