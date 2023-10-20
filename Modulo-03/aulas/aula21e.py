# Retornando Valores

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


resp1 = somar(3, 2, 5)
resp2 = somar(2, 2)
resp3 = somar(6)
print(f'Meus cálculos deram: {resp1}, {resp2}, {resp3}')
