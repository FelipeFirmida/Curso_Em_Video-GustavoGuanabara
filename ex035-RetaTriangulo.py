r1 = float(input('Qual o comprimento da primeira reta? '))
r2 = float(input('Qual o comprimento da segunda reta? '))
r3 = float(input('Qual o comprimento da terceira reta? '))

if ((r1+r2 > r3) and (r2+r3 > r1) and (r1+r3 > r2)):
    print('Essas retas cumprem com a condição de existência para formar um triângulo.')
else:
    print('Essas retas não cumprem com a condição de existência para formar um triângulo.')