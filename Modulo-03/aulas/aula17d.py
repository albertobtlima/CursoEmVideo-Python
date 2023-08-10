# Criar uma ligação entre listas:
# Todas as alterações um ums das lista se aplicará automaticamente a outra

a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('-' * 20)
# Criar uma cópia da lista:
# Alterações feitas em uma lista não afeta a outra.

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
