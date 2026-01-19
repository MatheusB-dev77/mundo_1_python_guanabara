"""n = str(input('Escreva uma frase:')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(n.count('A')))
print('A letra A apareceu na posição {}'.format(n.find('A') + 1))
print('A última letra A aparece na posição {}'.format(n.find('A')))"""

#professor guanabara

n = str(input('Escreva uma frase:')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(n.count('A')))
print('A letra A apareceu na posição {}'.format(n.find('A') + 1))
print('A última letra A aparece na posição {}'.format(n.rfind('A') + 1))


