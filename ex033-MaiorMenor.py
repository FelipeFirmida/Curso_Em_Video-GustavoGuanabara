n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o último número: '))
# procurar maior número
if (n1 >= n2):
    
    if (n1 >= n3):
        print('O maior número é {}'.format(n1))
    else:
        print('O maior número é {}'.format(n3))

else:

    if (n2 >= n3):
        print('O maior número é {}'.format(n2))
    else:
        print('O maior número é {}'.format(n3))

# procurar menor número
if (n1 <= n2):
    
    if (n1 <= n3):
        print('O menor número é {}'.format(n1))
    else:
        print('O menor número é {}'.format(n3))

else:

    if (n2 <= n3):
        print('O menor número é {}'.format(n2))
    else:
        print('O menor número é {}'.format(n3))
