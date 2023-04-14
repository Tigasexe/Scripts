from time import sleep

print('\033[32m———\033[m'*10)
print('       Tabuada de vezes')
print('\033[32m———\033[m'*10)

multiplicador = 1#10
'''while multiplicador <= 10:
    multiplicando = 1
    while multiplicando <= 10:
        print(multiplicador, 'x', multiplicando, '=', multiplicador * multiplicando)
        multiplicando += 1
    print('\033[34m———\033[m'*10)
    multiplicador += 1'''


while multiplicador <= 10:
    multiplicando = 1
    while multiplicando <= 10:
        print(f'{multiplicador} x {multiplicando} = {multiplicador * multiplicando}')
        multiplicando += 1
    sleep(2)
    print('\033[34m———\033[m'*10)
    multiplicador += 1

