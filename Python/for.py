'''1
#-------------inicio, fim, modo
from time import sleep
inicio = 1
quantidade = int(input('Digite uma quantidade: '))

while inicio <= quantidade:
    print(inicio)
    sleep(2)
    inicio += 1

print('Até a proxima!!')'''
'''2
while True:
    num = int(input('Digite um valor de "0" a "5" ou "12" para PARAR: '))
    if num == 0:
        print('Chute mais alto!!')
    elif num == 1:
        print('Obrigado!')
    elif num == 2:
        print('Beleza!')
    elif num == 3:
        print('Bacana!')
    elif num == 4:
        print('Showw')
    elif num == 5:
        print('Vinny')
    elif num == 12:
        print('Parar!!')
        exit()
    else:
        print('Esse numero é invalido. Tente novamente!!')'''