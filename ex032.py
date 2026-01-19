m = int(input('Qual ano você quer saber se é bissexto?'))
ano = m % 4 == 0
if ano == 0:
    print('Seu ano {} é bissexto'.format(ano))
else:
    print('Seu ano não é bissexto')