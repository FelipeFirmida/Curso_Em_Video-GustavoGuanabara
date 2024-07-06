frase = str(input('Digite uma frase: ')).strip()

countA = frase.upper().count('A')
firstA = frase.upper().find('A')
lastA = frase.upper().rfind('A')

print('A letra "A" aparece {} vezes na frase.'.format(countA))
print('A primeira vez que ela aparece é na posição {}.'.format(firstA + 1))
print('A última vez que ela aparece é na posição {}.'.format(lastA + 1))