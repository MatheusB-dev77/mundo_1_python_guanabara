n = float(input('Qual a distância da sua viagem'))
m = n * 0.50
o = n * 0.45
if n >= 100:
    print('Sua viagem custa {} reais'.format(m))
elif n <= 200:
    print('Sua viagem custa {} reais'.format(o))

#professor guanabara
distância = float(input('Qual a sua viagem?'))
print('Você está a começar uma viagem de {}km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

#ou
preço = distância * 0.50 if distância <= 200 else distância * 0.45