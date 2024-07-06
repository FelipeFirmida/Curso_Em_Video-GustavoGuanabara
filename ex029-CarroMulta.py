velocidade = int(input('Qual a velocidade do seu carro no momento? '))

multa = float((velocidade - 80) * 7)

if (velocidade > 80):
    print('Se ferrou, ultrapassou a velocidade máxima de 80km/h e foi multado! Sua multa é de R${:.2f}.'.format(multa))

else:
    print('Tudo certo! Você está dentro do limite de velocidade.')
