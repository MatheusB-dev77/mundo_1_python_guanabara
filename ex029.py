from time import sleep
vel = float(input('Qual a velocidade atual do carro?'))
print('-=-' * 20)
print('Tenha Cuidade! DIRIJA COM SEGURANÇA!')
print('-=-' * 20)
print('Processando')
sleep(2)

if vel <= 40:
    print('Sua velocidade ésta muito abaixo para esta pista')
elif vel <= 90:
    print('Sua Velocida está muito boa')
elif vel > 100:
    print('Reduza a Velocidade. Seu destino está logo alí')
    multa = (vel - 100) * 7
    print('Você deve pagar um multa de R${:.2f}'.format(multa))

#professor Guanabara

velocidade = float(input('Qual a velocidade atual do carro?'))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitidp que é 80km/h ')
    multa = (velocidade - 80) * 7
    print('Você deve pagar um multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')



