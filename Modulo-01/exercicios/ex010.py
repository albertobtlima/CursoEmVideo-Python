real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.92
euro = real / 5.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Ou com R${:.2f} você pode comprar ¢{:.2f}'.format(real, euro))
