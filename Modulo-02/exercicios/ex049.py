# Exercício 049 - Igual ao Exercício 009 do Modulo 01
# Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço FOR.

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
