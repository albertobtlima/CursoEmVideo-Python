# Exercício 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tebela abaixo:
# -> Abaixo de 18.5: abaixo do peso       -> 30 até 40: obesidade
# -> Entre 18.5 e 25: peso ideal          -> acima de 40: obesidade mórbida
# -> 25 até 30: sobrepeso

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal.')
elif 18.5 <= imc < 25:
    print('Você está na faixa de PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está na faixa de SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está na faixa de OBESIDADE.')
elif imc > 40:
    print('Você está na faixa de OBESIDADE MÓRBIDA.')
