#Bibliotecas importadas ----------------------------------

from hashlib import sha256 #Criptografia
from time import sleep #Tempo
from ia import Ia #POO
import string #Criar strings
import time #Tempo
import random #Randomizar Senha
import hashlib #Criptografia
import os.path

#Boas Vindas -----------------------------------
try:
    print('\033[33m-=\033[m'*15)
    print('   Seja Muito Bem Vindo(a) ')
    print('             Ao')
    print(' Nosso Sistema de Criptomoeda!')
    print('\033[33m-=\033[m'*20)

    time.sleep(0.2)

    ia = ''
    sexoia = ''

    #Sexo IA -----------------------------------
    ia = Ia()
    ia.esexoia()

    try:
        sexoia = int(input('Opção: '))
    except:
        print('Tente colocar um numero inteiro na proxima!')
        fechando = 'Fechando o sistema...'
        for letra in fechando:
            print('\033[31m' + letra + '\033[m', end='', flush=True)
            time.sleep(0.1)
        exit()

    while sexoia != 1 and sexoia != 2:
        print('Altenativa Inválida. Tente novamente!')
        ia.esexoia()

        try:
            sexoia = int(input('Opção: '))
        except:
            print('Tente colocar um numero inteiro na proxima!')
            fechando = 'Fechando o sistema...'
            for letra in fechando:
                print('\033[31m' + letra + '\033[m', end='', flush=True)
                time.sleep(0.1)
            exit()

    if sexoia == 1:
        ia.sexoiam()

        try:
            nomeia = int(input("Opção: "))
        except:
            print('Tente colocar um numero inteiro na proxima!')
            fechando = 'Fechando o sistema...'
            for letra in fechando:
                print('\033[31m' + letra + '\033[m', end='', flush=True)
                time.sleep(0.1)
            exit()
        while nomeia != 1 and nomeia != 2 and nomeia != 3 and nomeia != 4:
            print('Alternativa inválida. Tente novamente!!')
            ia.sexoiam()
            
            try:
                nomeia = int(input("Opção: "))
            except:
                print('Tente colocar um numero inteiro na proxima!')
                fechando = 'Fechando o sistema...'
                for letra in fechando:
                    print('\033[31m' + letra + '\033[m', end='', flush=True)
                    time.sleep(0.1)
                exit()

        if nomeia == 1:
            ia = "Jarvis"
        elif nomeia == 2:
            ia = "Alfred"
        elif nomeia == 3:
            ia = "Louis"
        elif nomeia == 4:
            ia = "Ziggy"

    elif sexoia == 2:
        ia.sexoiaf()
        
        try:
            nomeia = int(input("Opção: "))
        except:
            print('Tente colocar um numero inteiro na proxima!')
            fechando = 'Fechando o sistema...'
            for letra in fechando:
                print('\033[31m' + letra + '\033[m', end='', flush=True)
                time.sleep(0.1)
            exit()

        while nomeia != 1 and nomeia != 2 and nomeia != 3 and nomeia != 4:
            print("Alternativa inválida. Tente novamente!!")
            ia.sexoiaf()

            try:
                nomeia = int(input("Opção: "))
            except:
                print('Tente colocar um numero inteiro na proxima!')
                fechando = 'Fechando o sistema...'
                for letra in fechando:
                    print('\033[31m' + letra + '\033[m', end='', flush=True)
                    time.sleep(0.1)
                exit()

        if nomeia == 1:
            ia = "Aurora"
        elif nomeia == 2:
            ia = "Serena"
        elif nomeia == 3:
            ia = "Athena"
        elif nomeia == 4:
            ia = "Iris"

    #Conversação -----------------------------------

    frase1 = f'{ia}: Olá me chamo {ia} eu sou a inteligencia artificial do Sistema de Criptomoeda!'
    for letra in frase1:
        print(letra, end='', flush=True)
        time.sleep(0.03)

    try:
        nome = str(input(f'\n{ia}: Qual o seu nome ? ')).strip()
    except:
        print('Tente colocar um numero inteiro na proxima!')
        fechando = 'Fechando o sistema...'
        for letra in fechando:
            print('\033[31m' + letra + '\033[m', end='', flush=True)
            time.sleep(0.1)
        exit()

    dnome = nome.split()

    if len(nome) == 0:
        print('Tente colocar um numero inteiro na proxima!')
        fechando = 'Fechando o sistema...'
        for letra in fechando:
            print('\033[31m' + letra + '\033[m', end='', flush=True)
            time.sleep(0.1)
        exit()

    if nome.lower() == ia.lower():
        conv1 = f'{ia}: Nossa que nome bonito hehe!'
        for letra in conv1:
            print(letra, end='', flush=True)
            time.sleep(0.03)
    else:
        conv1 = f'{ia}: É um prazer conhecer você {dnome[0]}'
        for letra in conv1:
            print(letra, end='', flush=True)
            time.sleep(0.03)
    print('')

    #Menu do Sistema -----------------------------------

    code1 = '10 reais'
    code2 = '20 reais'
    code3 = '30 reais'
    code4 = '40 reais'
    code5 = '50 reais'
    code6 = '60 reais'
    code7 = '70 reais'
    code8 = '80 reais'
    code9 = '90 reais'
    code10 = '100 reais'

    cripto1 = sha256(code1.encode()).hexdigest()
    cripto2 = sha256(code2.encode()).hexdigest()
    cripto3 = sha256(code3.encode()).hexdigest()
    cripto4 = sha256(code4.encode()).hexdigest()
    cripto5 = sha256(code5.encode()).hexdigest()
    cripto6 = sha256(code6.encode()).hexdigest()
    cripto7 = sha256(code7.encode()).hexdigest()
    cripto8 = sha256(code8.encode()).hexdigest()
    cripto9 = sha256(code9.encode()).hexdigest()
    cripto10 = sha256(code10.encode()).hexdigest()

    valor_moeda = 0.00094 
    valor_transferencia = 0

    while True:

        print('\033[34m-=\033[m'*15)
        print('Oque você deseja fazer nesse sistema?')
        print('[ 1 ] - Minerar')
        print('[ 2 ] - Transferir')
        print('[ 3 ] - Ver Saldo')
        print('[ 0 ] - Sair!!')
        print('\033[34m-=\033[m'*15)
        try:
            op = int(input('Opção: '))
        except:
            print('Tente colocar um numero inteiro na proxima!')
            fechando = 'Fechando o sistema...'
            for letra in fechando:
                print('\033[31m' + letra + '\033[m', end='', flush=True)
                time.sleep(0.1)
            exit()
            
        if op == 0:
            print('Tchau, Tchau', end='')
            for _ in range(3):
                print('.', end='', flush=True)
                sleep(0.8)
            exit()
    #Condição de erro -----------------------------------

        elif op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
            print('Alternativa inválida. Tente novamente!')

    #Sistema de Mineração -----------------------------------

        elif op == 1:

            print('A mineração começará em...')
            
            for cont in range(5, 0, -1):
                print(cont)
                sleep(1)

            def gerador_de_senhas(tamanho):
                caracteres = string.ascii_letters + string.digits
                return ''.join(random.choice(caracteres) for c in range(tamanho))

            def sha256_hash(texto):
                return hashlib.sha256(texto.encode('utf-8')).hexdigest()

            tamanho_chave = 64
            tentativas = 0

            find = []

            while True:
                tentativas += 1
                chave_random = gerador_de_senhas(tamanho_chave)
                chave_hashed = sha256_hash(chave_random)

                if chave_hashed == cripto1:
                    find_discript = os.path.isfile('Discripto.txt')

                    if find_discript == True:
                        with open('Discripto.txt', 'r') as modify:
                            modificar = modify.read()
                            to_modify = float(modificar)
                        with open('Discripto.txt', 'w') as alterar:
                            alterar.write(f'{to_modify + 10}')
                    else:
                        with open('Discripto.txt', 'w') as dinheiro:
                            dinheiro.write('10')
                    print('\033[32m' + cripto1 + '\033[m')
                    print(f'A chave foi encontrada com {tentativas} tentativas')
                    find.append(chave_hashed)
                    break
                elif chave_hashed == cripto2:
                    find_discript = os.path.isfile('Discripto.txt')

                    if find_discript == True:
                        with open('Discripto.txt', 'r') as modify:
                            modificar = modify.read()
                            to_modify = float(modificar)
                        with open('Discripto.txt', 'w') as alterar:
                            alterar.write(f'{to_modify + 20}')
                    else:
                        with open('Discripto.txt', 'w') as dinheiro:
                            dinheiro.write('20')
                    print('\033[32m' + cripto2 + '\033[m')
                    print(f'A chave foi encontrada com {tentativas} tentativas')
                    find.append(chave_hashed)
                    break
                elif chave_hashed == cripto3:
                    find_discript = os.path.isfile('Discripto.txt')

                    if find_discript == True:
                        with open('Discripto.txt', 'r') as modify:
                            modificar = modify.read()
                            to_modify = float(modificar)
                        with open('Discripto.txt', 'w') as alterar:
                            alterar.write(f'{to_modify + 30}')
                    else:
                        with open('Discripto.txt', 'w') as dinheiro:
                            dinheiro.write('30')
                    print('\033[32m' + cripto3 + '\033[m')
                    print(f'A chave foi encontrada com {tentativas} tentativas')
                    find.append(chave_hashed)
                    break
                elif chave_hashed == cripto4:
                    find_discript = os.path.isfile('Discripto.txt')

                    if find_discript == True:
                        with open('Discripto.txt', 'r') as modify:
                            modificar = modify.read()
                            to_modify = float(modificar)
                        with open('Discripto.txt', 'w') as alterar:
                            alterar.write(f'{to_modify + 40}')
                    else:
                        with open('Discripto.txt', 'w') as dinheiro:
                            dinheiro.write('40')
                    print('\033[32m' + cripto4 + '\033[m')
                    print(f'A chave foi encontrada com {tentativas} tentativas')
                    find.append(chave_hashed)
                    break
                elif chave_hashed == cripto5:
                    find_discript = os.path.isfile('Discripto.txt')

                    if find_discript == True:
                        with open('Discripto.txt', 'r') as modify:
                            modificar = modify.read()
                            to_modify = float(modificar)
                        with open('Discripto.txt', 'w') as alterar:
                            alterar.write(f'{to_modify + 50}')
                    else:
                        with open('Discripto.txt', 'w') as dinheiro:
                            dinheiro.write('50')
                    print('\033[32m' + cripto5 + '\033[m')
                    print(f'A chave foi encontrada com {tentativas} tentativas')
                    find.append(chave_hashed)
                    break
                elif chave_hashed == cripto6:
                    find_discript = os.path.isfile('Discripto.txt')

                    if find_discript == True:
                        with open('Discripto.txt', 'r') as modify:
                            modificar = modify.read()
                            to_modify = float(modificar)
                        with open('Discripto.txt', 'w') as alterar:
                            alterar.write(f'{to_modify + 60}')
                    else:
                        with open('Discripto.txt', 'w') as dinheiro:
                            dinheiro.write('60')
                    print('\033[32m' + cripto6 + '\033[m')
                    print(f'A chave foi encontrada com {tentativas} tentativas')
                    find.append(chave_hashed)
                    break
                elif chave_hashed == cripto7:
                    find_discript = os.path.isfile('Discripto.txt')

                    if find_discript == True:
                        with open('Discripto.txt', 'r') as modify:
                            modificar = modify.read()
                            to_modify = float(modificar)
                        with open('Discripto.txt', 'w') as alterar:
                            alterar.write(f'{to_modify + 70}')
                    else:
                        with open('Discripto.txt', 'w') as dinheiro:
                            dinheiro.write('70')
                    print('\033[32m' + cripto7 + '\033[m')
                    print(f'A chave foi encontrada com {tentativas} tentativas')
                    find.append(chave_hashed)
                    break
                elif chave_hashed == cripto8:
                    find_discript = os.path.isfile('Discripto.txt')

                    if find_discript == True:
                        with open('Discripto.txt', 'r') as modify:
                            modificar = modify.read()
                            to_modify = float(modificar)
                        with open('Discripto.txt', 'w') as alterar:
                            alterar.write(f'{to_modify + 80}')
                    else:
                        with open('Discripto.txt', 'w') as dinheiro:
                            dinheiro.write('80')
                    print('\033[32m' + cripto8 + '\033[m')
                    print(f'A chave foi encontrada com {tentativas} tentativas')
                    find.append(chave_hashed)
                    break
                elif chave_hashed == cripto9:
                    find_discript = os.path.isfile('Discripto.txt')

                    if find_discript == True:
                        with open('Discripto.txt', 'r') as modify:
                            modificar = modify.read()
                            to_modify = float(modificar)
                        with open('Discripto.txt', 'w') as alterar:
                            alterar.write(f'{to_modify + 90}')
                    else:
                        with open('Discripto.txt', 'w') as dinheiro:
                            dinheiro.write('90')
                    print('\033[32m' + cripto9 + '\033[m')
                    print(f'A chave foi encontrada com {tentativas} tentativas')
                    find.append(chave_hashed)
                    break
                elif chave_hashed == cripto10:
                    find_discript = os.path.isfile('Discripto.txt')

                    if find_discript == True:
                        with open('Discripto.txt', 'r') as modify:
                            modificar = modify.read()
                            to_modify = float(modificar)
                        with open('Discripto.txt', 'w') as alterar:
                            alterar.write(f'{to_modify + 100}')
                    else:
                        with open('Discripto.txt', 'w') as dinheiro:
                            dinheiro.write('100')
                    print('\033[32m' + cripto10 + '\033[m')
                    print(f'A chave foi encontrada com {tentativas} tentativas')
                    find.append(chave_hashed)
                    break
                else:
                    print('\033[31m' + chave_hashed + '\033[m')
                    sleep(0.1)
            
            with open('Cripto.txt', 'w') as save:
                save.write(''.join(map(str, find)))
            
    #Transferencia -----------------------------------        
        
        elif op == 2:

            while True:
                print('\033[34m-=\033[m'*25)
                print('Escolha para quem você vai fazer Transferência!')
                print('[ 1 ] - Daniel')
                print('[ 2 ] - Laura')
                print('[ 3 ] - Matheus')
                print('[ 4 ] - Roberto')
                print('[ 5 ] - Isa')
                print('[ 0 ] - Voltar')
                print('\033[34m-=\033[m'*25)
                try:
                    transferencia = int(input("Opção: "))
                except:
                    print('Tente colocar um numero inteiro na proxima!')
                    fechando = 'Fechando o sistema...'
                    for letra in fechando:
                        print('\033[31m' + letra + '\033[m', end='', flush=True)
                        time.sleep(0.1)
                    exit()
                if transferencia == 0:
                    print('Saindo', end='')
                    for _ in range(3):
                        print('.', end='', flush=True)
                        sleep(0.8)
                    print('')
                    break

    #Condição de erro -----------------------------------

                elif transferencia != 1 and transferencia != 2 and transferencia != 3 and transferencia != 4 and transferencia != 5:
                    print("Alternativa Inválida!!")

    #----------------------------------------------------
                else:
                    valor_transferencia = float(input("Valor da Transfencia: R$"))
                    print(f'R${valor_transferencia} em criptomoeda será {valor_moeda * valor_transferencia}Jz')

                    print('\033[34m-=\033[m'*25)
                    print('Você tem certeza que quer continuar?')
                    print('[ 1 ] - Sim')
                    print('[ 2 ] - Não')
                    print('\033[34m-=\033[m'*25)
                    try:
                        verificar = int(input('Opção: '))
                    except:
                        print('Tente colocar um numero inteiro na proxima!')
                        fechando = 'Fechando o sistema...'
                        for letra in fechando:
                            print('\033[31m' + letra + '\033[m', end='', flush=True)
                            time.sleep(0.1)
                        exit()

                    match verificar:
                        case 1:
                            find_arq = os.path.isfile('Discripto.txt')

                            if find_arq == True:

                                with open('Discripto.txt', 'r') as arquivo_descriptografado:
                                    dinheiro = arquivo_descriptografado.read()

                                money_convert = float(dinheiro)
                                if money_convert - valor_transferencia >= 0:
                                    with open('Discripto.txt', 'w') as arquivo_descriptografado:
                                        arquivo_descriptografado.write(f'{money_convert - valor_transferencia}')

                                    print('Ok. Transação completa!')
                                else:
                                    print(f'A transação não pôde ser completada.\nVocê tem apenas R${money_convert} para fazer uma transação de R${valor_transferencia}!!')
                                    break
                            else:
                                print('\033[31mNão foi possivel encontrar seu saldo. Tente minerar primeiro!')
                                break
                        case 2:
                            print('Cancelando Transação', end='')
                            for _ in range(3):
                                print('.', end='', flush=True)
                                time.sleep(0.3)
                            print('')
                            break
                        case _:
                            invalida = '\033[31mAlternativa inválida!\033[m'
                            for letra in invalida:
                                print(letra, end='', flush=True)
                                time.sleep(0.09)
                            print()

    #Ver Saldo -------------------------------------------

        elif op == 3:
            find_past = os.path.isfile('Cripto.txt')

            if find_past == True:
                with open('Cripto.txt', 'r') as arquivo_criptografado:
                    read_past = arquivo_criptografado.read()
                with open('Discripto.txt', 'r') as arquivo_descriptografado:
                        read_discripto = arquivo_descriptografado.read()

                convert = float(read_discripto)      

                if read_past == cripto1:
                    with open('Discripto.txt', 'r') as read_discripto:
                        read_discripto.read()
                    print(f'Seu saldo é de R${convert} em Cripto você tem {valor_moeda * convert}Jz')
                elif read_past == cripto2:
                    with open('Discripto.txt', 'r') as read_discripto:
                        read_discripto.read()
                    print(f'Seu saldo é de R${convert} em Cripto você tem {valor_moeda * convert}Jz')
                elif read_past == cripto3:
                    with open('Discripto.txt', 'r') as read_discripto:
                        read_discripto.read()
                    print(f'Seu saldo é de R${convert} em Cripto você tem {valor_moeda * convert}Jz')
                elif read_past == cripto4:
                    with open('Discripto.txt', 'r') as read_discripto:
                        read_discripto.read()
                    print(f'Seu saldo é de R${convert} em Cripto você tem {valor_moeda * convert}Jz')
                elif read_past == cripto5:
                    with open('Discripto.txt', 'r') as read_discripto:
                        read_discripto.read()
                    print(f'Seu saldo é de R${convert} em Cripto você tem {valor_moeda * convert}Jz')
                elif read_past == cripto6:
                    with open('Discripto.txt', 'r') as read_discripto:
                        read_discripto.read()
                    print(f'Seu saldo é de R${convert} em Cripto você tem {valor_moeda * convert}Jz')
                elif read_past == cripto7:
                    with open('Discripto.txt', 'r') as read_discripto:
                        read_discripto.read()
                    print(f'Seu saldo é de R${convert} em Cripto você tem {valor_moeda * convert}Jz')
                elif read_past == cripto8:
                    with open('Discripto.txt', 'r') as read_discripto:
                        read_discripto.read()
                    print(f'Seu saldo é de R${convert} em Cripto você tem {valor_moeda * convert}Jz')
                elif read_past == cripto9:
                    with open('Discripto.txt', 'r') as read_discripto:
                        read_discripto.read()
                    print(f'Seu saldo é de R${convert} em Cripto você tem {valor_moeda * convert}Jz')
                elif read_past == cripto10:
                    with open('Discripto.txt', 'r') as read_discripto:
                        read_discripto.read()
                    print(f'Seu saldo é de R${convert} em Cripto você tem {valor_moeda * convert}Jz')

            else:
                print('\033[31mO arquivo "Cripto.txt" não existe. Tente encontrar alguma Criptomoeda primeiro!\033[m')
except:
    print('\nO sistema está fechando pós um erro!')