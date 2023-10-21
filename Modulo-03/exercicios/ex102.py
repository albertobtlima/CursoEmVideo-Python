# Exercício 102
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
# número a calcular e o outro chamado show, que  será um valor lógico (opcional) indicando  se  será
# mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


num = int(input('Digite um número: '))
resp = str(input('Quer ver o calculo? [S/N] ')).upper()
if resp == 'S':
    show = True
else:
    show = False
print(fatorial(num, show))
