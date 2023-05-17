from random import randint
from time import sleep

print('\033[33m-=-=-\033[m'*13)
print('\033[34mVou pensar em um numero entre 0 e 5. Tente Adivinhar...')
print('\033[33m-=-=-\033[m'*13)

pc = randint(0, 5) 

player = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...\033[m')
sleep(1.5)
if player == pc:
    print('\033[33mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[31mGANHEI! Eu pensei no numero {} e não no {}\033[m'.format(pc, player))