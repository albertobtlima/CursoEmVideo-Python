def aumentar(preco=0, taxa=0, formato=False):
    """
       -> Calcula o aumento de um determinado preço, retornando o resultado com ou sem formatação.
       :param preco: o preço que se quer reajustar.
       :param taxa: qual é a porcetagem do aumento.
       :param formato: quer a saída formatada ou não.
       :return: o valor reajustado, com ou sem formatação.
       """
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaAumento=10, taxaReducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaAumento}% de aumento: \t{aumentar(preco, taxaAumento, True)}')
    print(f'{taxaReducao}% de redução: \t{diminuir(preco, taxaReducao, True)}')
    print('-' * 30)
