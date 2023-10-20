def parOuImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if parOuImpar(num):
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é impar!')
