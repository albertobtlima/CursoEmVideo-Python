estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print('-=' * 15)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
