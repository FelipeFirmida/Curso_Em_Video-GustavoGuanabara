from math import hypot

x = float(input('Digite o comprimento do cateto oposto: '))
y = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = hypot(x, y)

print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))