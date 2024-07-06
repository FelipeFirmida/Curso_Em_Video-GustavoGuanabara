from math import sin, cos, tan, radians

n = float(input('Digite um ângulo: '))

seno = sin(radians(n))
cosseno = cos(radians(n))
tangente = tan(radians(n))

print('O ângulo {} possui o seno de {:.4f}, o cosseno de {:.4f} e a tangente de {:.4f}.'.format(n, seno, cosseno, tangente))