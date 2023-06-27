from random import randint
from time import sleep

#Cabeçalho
print('\033[36m-=-\033[m'*15)
print('{:^46}'.format('\033[33mJogo Do Acerto!'))
print('\033[36m-=-\033[m'*15)

#Opções iniciais
print('[ 1 ] Inciar!')
print('[ 2 ] Não Iniciar!')
op = int(input('Opção: '))

#Condições
while op != 1 and op != 2:
    print('[ 1 ] Inciar!')
    print('[ 2 ] Não Iniciar!')
    op = int(input('Opção: '))
    
if op == 1:
    def acertou():
        texto = 'Parabéns Você acertou o numero!!'
        for letra in texto:
            print(letra, end='', flush=True)
            sleep(0.05)
        print()
        for c in range(0, 5):
            print(f'\033[3{c + 1}m{c + 1}')
            sleep(0.5)

        texto = '\033[32mBUM!🎊 \033[33mBUM!🎉 \033[34mBUM!🥳\033[m'
        for letra in texto:
            print(letra, end='', flush=True)
            sleep(0.05)

    print('Criando o numero Secreto', end='')
    texto = '...'

    for letras in texto:
        print(letras, end='', flush=True)
        sleep(0.3)
    
    mTempo = 0
    partida = 0

    def jogo():
        numero_secreto = randint(0, 100)
        tentativas = 0
        while True:
            user = int(input(f'\nEscreva um numero no intervalo de (0, 100):{numero_secreto} '))
            tentativas += 1

            if user < 0 or user > 100:
                print('\033[31mEscolha um numero dentro do intervalo!\033[m')
            elif user > numero_secreto:
                print('Dica:\033[31mTente Um numero Menor!\033[m')
            elif user < numero_secreto:
                print('Dica:\033[32mTente Um numero Maior!\033[m')
            elif user == numero_secreto:
                acertou()
                print('\nVocê quer continuar jogando?')
                print('[ 1 ] Sim!')
                print('[ 2 ] Não!')
                op2 = int(input('Opção: '))
                global partida
                partida += 1

                if partida == 1:
                    global mTempo
                    mTempo = tentativas
                elif partida > 1:
                    if mTempo > tentativas:
                        mTempo = tentativas
                while op2 != 1 and op2 != 2:
                    print('Não existe essa opção!')
                    print()
                    print('\nVocê quer continuar jogando?')
                    print('[ 1 ] Sim!')
                    print('[ 2 ] Não!')
                    op2 = int(input('Opção: '))

                if op2 == 1:
                    print('\033[34m-=-\033[m'*15)
                    return jogo()
                else:
                    print(f'Você jogou {partida} Partidas e o seu melhor tempo foi de {mTempo} Tentativas!')
                    print('Obrigado Por Jogar Nosso Jogo!')
                    break
    jogo()
else:
    print('Até mais!')
    exit()