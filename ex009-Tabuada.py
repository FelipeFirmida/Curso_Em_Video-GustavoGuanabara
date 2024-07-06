n = int(input('Digite um número inteiro: '))

tab = 0
resultado = 0
for tab in range(1 , 10):
    resultado = n * tab
    print('{} * {:2} = {}'.format(n, tab, resultado))