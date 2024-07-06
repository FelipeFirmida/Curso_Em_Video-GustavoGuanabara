import secrets
aluno = []
for x in range(4):
    aluno.append(input('Qual o nome do aluno: '))

print('O aluno escolhido para apagar o quadro foi {}.'.format(secrets.choice(aluno)))