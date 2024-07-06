nome = input('Digite seu nome completo: ')

print('O nome em letras minúsculas é: {}'.format(nome.lower()))
print('O nome em letras maiúsculas é: {}'.format(nome.upper()))
print('A quantidade de letras nesse nome completo é de {}'.format(len(nome) - nome.count(" ")))

split = nome.split()

print('O primeiro nome tem {} letras.'.format(len(split[0])))
