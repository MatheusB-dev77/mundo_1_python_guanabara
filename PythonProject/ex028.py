print('Vou pensar num número entre 0 e 5. tente adivinhar...')
n = float(input('En que número pensei ?'))
if n == 0:
    print('Parabéns! você acertou o número')
else:
    print('Você errou. Não foi esse número que pensei.')


# professor guanabara

from random import randint
from time import sleep
computador = randint(0,1)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))#jogador tanta advinahr
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('parabéns! Você acertou e conseguiu me vencer')
else:
    print('Ganhei de VOCÊ!!!!')

