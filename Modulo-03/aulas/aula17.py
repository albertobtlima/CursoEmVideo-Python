num = [2, 5, 9, 1]
print(num)
num[2] = 3 # Troca o item na lista
print(num)
num.append(7) # Adiciona o item ao final da lista
print(num)
num.sort() # Ordena a lista
print(num)
num.sort(reverse=True) # Inverte a lista
print(num)
num.insert(2, 0) # Adiciona o item na posição indicada
print(num)
num.pop(2) # Deleta o item na posição indicada, se deixado em branco o ultimo item será deletado
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(f'Essa lista tem {len(num)} elementos.')
