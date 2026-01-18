"""n = str(input('Digite seu nome completo:'))
print('''''')
print('Seu nome em maiúscula é {}'. format(n.upper()))
print('Seu nome em minúscula é {}'.format(n.lower()))
print('seu nome tem ao todo {} letras'.format(len(n.strip())))
print('Seu primeiro nome é {} e ele tem {} letras'.format(n.split()[0], len(n.split())))"""

#guanabara
n = str(input('Digite seu nome completo:')).strip()
print("""Analisando seu nome ...""")
print('Seu nome em maiúscula é {}'. format(n.upper()))
print('Seu nome em minúscula é {}'.format(n.lower()))
print('seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
m = n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(m[0], len(m[0])))

