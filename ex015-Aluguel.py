km = float(input('Quantos Km foram percorridos com o carro? '))
dias = int(input('Quantos dias o carro foi alugado? '))

resultado = (km * 0.15) + (dias * 60)

print('Como você percorreu {} Km por {} dias de aluguel, o valor total é R$ {:.2f}'.format(km, dias, resultado))