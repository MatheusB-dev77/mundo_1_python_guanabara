
'''\033(0;33;44m
#style  vai do 0,1, 4, 7(nome, bold, underline, negative)
#text vai do 30, 31,31, 33, 34, 35, 36, 37
#back vai do 40 ao 47
\033(0;30;41m
\033(4;33;44m
\033(1;35;43m
\033(30;42m
\033(m
\033(7;30m'''

print('\033[4;30;45mOlá mundo!\033[m')
print('\033[0;30;44mOlá mundo!\033[m')

a = 3
b = 5
print('os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))
nome = 'guanabara'
cores = {'limpa':'\033[34m',}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome, '\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))

