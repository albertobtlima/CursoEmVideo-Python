# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando {moeda.moeda(preco)} em 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo {moeda.moeda(preco)} em 13%, temos {moeda.diminuir(preco, 13, True)}')
