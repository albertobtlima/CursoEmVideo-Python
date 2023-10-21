# Exercício 104
# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função
# input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaint('Digite um número: ').

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


num = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número: {num}')
