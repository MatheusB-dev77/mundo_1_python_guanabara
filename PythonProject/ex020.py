'''import random

n = str(input('Digite um nome de um aluno: '))
m = str(input('Digite um nome de um aluno: '))
s = str(input('Digite um nome de um aluno: '))
o = str(input('Digite um nome de um aluno: '))
lista = [n, m, s, o]
random.shuffle(lista)
print('A nova ordem de apresentação deve ser essa {}'.format(lista))'''

#professor guanabara

from random import shuffle
n1 = str(input('Digite um nome de um aluno: '))
n2 = str(input('Digite um nome de um aluno: '))
n3 = str(input('Digite um nome de um aluno: '))
n4 = str(input('Digite um nome de um aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)