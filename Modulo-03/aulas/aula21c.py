# Escopo de variáveis
# --------------------------

def teste():
    x = 8                                          # variavel local
    print(f'Na funçaõ teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa principal
n = 2                                              # variavel global
print(f'No programa principal, n vale {n}')
teste()
