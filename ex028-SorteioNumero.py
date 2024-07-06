from random import randint

n = int(input('Em que número de 0 a 5 eu estou pensando? '))

random = randint(0,5)

if (random == n):
    print('Parabéns, você acertou!')

else:
    print('Você errou! Eu estava pensando no {}'.format(random))