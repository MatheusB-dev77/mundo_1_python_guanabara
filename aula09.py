#fatiamento

'''frase = 'Curso em vídeo Python'
frase[9]
frase[9:12]
frase[9:21:2]
#pula de dois em dois  e ignora o sempre o segundo
frase[:5]
#quano omito o primeiro carácter, sempre começa do inicio
frase[15:] #pega do caracter 15 até o final da frase
frase[9::3]# começa do caracter 9 até o final da frase. O 3 significa que vai pular três casa e sempre mostrará o
# terceiro caracter
len(frase)# analisa a quantidade de caracter da frase
frase.count('o')#pede para que o pytho conte quantos 'o' minusculo tem na frase.
frase.count('o',0,13) #considera do zero ao treze, e mostra a quantidade de letra zero
frase.find('deo')# quantas vezes ele encontra o 'deo' e diz sua posição no inicio
frase.find('Android')# retorna o valor -1 quando não encontraovalor procurado na frase
frase.rfind procura pell fim
'curso' in frase# escreve true ou false dependendo se existe ou não esse valor na frase

#tranformação

frase.replace('Python', 'Android')#subistitui a palavra ýthon pór android
frase.upper()#deixa maiúsculo o que não estava
frase.lower()# substitui o maiusculo para minusculo
frase.capitalize()# joga tudo para minusculo e coloca a primeira letra em maiuscula da primeira palavra
frase.title()# analisa quantas palavras tem e transforma todas as primeiras letras da frase me maiúscula
frase.strip()# remove espaços inuteis do inicio e final da str
frase.lstrip()# remove espaços da esquerda
frase.rstrip()# remove espaços da direita
frase.split()# divide a string em lista
'-'.join(frase)# coloca - entre os espaços'''

frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[13:9])
print(frase[1:15:2])
print(frase[9::3])
print(frase[::2])
print('''gdwqoiuefgweifug''')
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.find('Android'))
print(frase.lower().find('vídeo'))
print(frase.replace('Python', 'Android'))
print(frase.split())
dividido = frase.split()
print(dividido[2] [3])





