km = int(input('Quantos Km de distância tem a sua viagem? '))

if (km <= 200):
    custo = float(km * 0.5)
else:
    custo = float(km * 0.45)

print('A sua passagem custará R$ {:.2f}.'.format(custo))