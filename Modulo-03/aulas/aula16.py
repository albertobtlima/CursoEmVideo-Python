# variável -> Tupla
# Tuplas são variáveis imutaveis
# A Tupla pode ser deletada com o comando del(nome da variável)

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print('-' * 30)

print(lanche)
print(sorted(lanche))
print('-' * 30)

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-' * 30)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição -> {cont}')
print('-' * 30)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição -> {pos}')
print('-' * 30)

print('Comi pra caramba!')
