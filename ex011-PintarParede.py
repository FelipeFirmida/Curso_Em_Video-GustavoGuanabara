largura = int(input('Qual a largura em metros da parede? '))
altura = int(input('Qual a altura em metros da parede? '))

area = largura * altura
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {} metros quadrados.'.format(largura, altura, area))
print('Você precisará de {} litros de tinta para pintar essa parede.'.format(tinta))