salario = float(input('Qual o seu salário? '))

if (salario > 1250):
    print('Seu salário será aumentado para R${:.2f}'.format(salario*1.1))

else:
    print('Seu salário será aumentado para R${:.2f}'.format(salario*1.15))