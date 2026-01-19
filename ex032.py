m = int(input('Qual ano você quer saber se é bissexto?'))
ano = m % 4 == 0
if ano == 0:
    print('Seu ano {} é bissexto'.format(ano))
else:
    print('Seu ano não é bissexto')

#professor guanabara
from datetime import date
ano = int(input('Que ano quer analisar'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))
