import random

alunos = []
for x in range (4):
    alunos.append(input('Digite o nome do aluno {}: '.format(x+1)))

random.shuffle(alunos)

print('A ordem sorteada para apresentação dos trabalhos será: {}'.format(alunos))