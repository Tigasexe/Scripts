from random import sample
from time import sleep

aMax = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
aMin = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
cEsp = '!@#$%&*:/?'

junction = aMax + aMin + num + cEsp
amount = 15

def function():
    print('-=-'*10)
    print('Password Generate')
    print('-=-'*10)
    
    question = int(input('Digite quantas senhas você quer gerar: '))
    passwords = []

    if question > 1:
        print('As senhas geradas são essas...')
        sleep(2)
    for c in range(1, question + 1):
        senha = ''.join(sample(junction, amount))
        print(f'Senha {c}: {senha}')
        passwords.append(senha)


    for n in range(len(passwords)):
        print('-=-'*10)
        print(f'{n + 1} Para senha: {passwords[n]}')
        print('-=-'*10)

    s = int(input('Digite uma opção: '))
    arquivo = open(f'Senha{s}.txt', 'w')
    arquivo.write(f'{passwords[s-1]}\n')
        

function()

