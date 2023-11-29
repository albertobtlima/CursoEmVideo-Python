# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número Inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número Real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
        else:
            return n


num1 = leiaInt('Digite um número Inteiro: ')
num2 = leiaFloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {num1} e o Real foi {num2}')
