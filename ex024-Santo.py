city = str(input('Digite o nome de uma cidade: ')).strip()
if (city.upper().startswith('SANTO') == True):
    print('A cidade {} começa com "SANTO".'.format(city))
else:
    print('A cidade {} não começa com "SANTO".'.format(city))