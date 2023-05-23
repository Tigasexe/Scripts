from random import randint
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
computer = randint(0, 2)
print('O computador escolheu {}'.format(lista[computer]))
print('Suas Opções:')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
jogador = int(input('Qual e a Sua Jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
sleep(1)
print('=-'*15)
print('Computador Jogou {}'.format(lista[computer]))
print('Jogador Jogou {}'.format(lista[jogador - 1]))
print('=-'*15)

if computer == jogador -1:
    print('Jogadas Iguais!!')
elif computer == 0 and jogador -1 == 1 or computer == 1 and jogador -1 == 2 or computer == 2 and jogador -1 == 0:
    print('Jogador Ganhouu')
else:
    print('Computador Venceu!!!')
