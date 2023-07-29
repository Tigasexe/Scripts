from random import randint

print('Sou seu computador...')
computador = randint(0, 10)
print('Acabdei de pensar em um numero entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
tentativas = 0
while True:
    player = int(input('Qual é seu palpite? '))
    tentativas += 1

    if player < 0 or player > 10:
        print('Dados Inválidos. Tente novamente!')
        tentativas -= 1
    elif player > computador:
        print('Menos... Tente mais uma vez.')
    elif player < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print('Acertou com {} tentativas'.format(tentativas))
        break