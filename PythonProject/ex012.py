n = float(input('Digite o valor do produto: R$'))
print('Seu produto custa R$ {}, mas com o desconto de 5% passará a custar R$ {}'.format(n, n - (n * 0.05)))

#Professor Guanabara
preço = float(input('Qual é o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
print(' O preço do produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(preço, novo))