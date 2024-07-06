numero = int(input('Digite um número de 0 a 9999: '))
if (numero < 0 or numero > 9999):
    print('Número digitado fora do range. Tente novamente.')
    numero = int(input('Digite um número de 0 a 9999: '))
else:
    digitos = []
    for x in range(4):
        digitos.append(numero % 10)
        numero = int(numero / 10)

print("""Os digitos do respectivo número são:
      unidade: {}
      dezena:  {}
      centena: {}
      milhar:  {}""".format(digitos[0], digitos[1], digitos[2], digitos[3]))
