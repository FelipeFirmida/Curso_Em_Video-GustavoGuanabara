nome = str(input('Digite seu nome completo: ')).strip()

split = nome.split()
primeiro = split[0]
último = split[len(split)-1]

print("""      Seu nome completo é {}.
      Seu primeiro nome é {}.
      Seu último nome é {}.""".format(nome, primeiro, último))