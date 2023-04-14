from time import sleep

a = str(input('Você é usuario de linux? '))
vezes = 0

while vezes <= 15:

    if a.lower() == 'sim':
        print()
        print('Nossa me surpreendeu!!')
        sleep(1)
        print('Qual linux você usa?')
        print('[ 1 ] Mint')
        print('[ 2 ] Ubuntu')
        print('[ 3 ] Debian')
        print('[ 4 ] Kali')
        print('[ 5 ] Outros...')
        print('[ 6 ] Parar!!')
        p1 = int(input('Digite uma alternativa: '))
        vezes += 1

        if p1 == 1:
            print('Nossa, Boa escola!')
            p2 = str(input('Você está gostando do mint? '))

            if p2.lower() == 'sim':
                print('Que bom que está gostando!!')
            else:
                print('Ahhh... Que pena, Que tal outra distro?')
        
        elif p1 == 2:
            print('Ubuntu está na minha lista de melhores distros. Boa escolha!!')
        
        elif p1 == 3:
            print('Debian... Falam muito bem dele, más, nunca testei.')
            p3 = str(input('É uma boa distro? '))

            if p3.lower() == 'sim':
                print('Muito bom saber.')
            else:
                print('Ahh... Ok. Obrigado pela informação!!')

        elif p1 == 4:
            print('Uhmmm... Vou lembrar de tomar cuidado com você. ;)')

        elif p1 == 5:
            p4 = str(input('Qual Linux você usa? '))
            print('Carregando...')
            sleep(2)
            print(f'Linux {p4}? Obrigado por nos contar!!')
        
        elif p1 == 6:
            print('Até mais...')
            exit()

        else:
            print('Não existe essa alternativa. Tente novamente!!')
            vezes -= 1

    else:
        print('''Windows foi detectado...
    "Avast."''')
        print()
        vezes += 16
        

print('Agradecemos sua interação. Até a proxima!!')