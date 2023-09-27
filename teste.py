#Bibliotecas importadas ----------------------------------

from hashlib import sha256 #Criptografia
from time import sleep #Tempo
import string #Criar strings
import time #Tempo
import random #Randomizar
import hashlib #Criptografia
import os.path #Sistema Operacional | Procurar Pasta

#Boas Vindas -----------------------------------
try:
    print('\033[34m-=\033[m'*20)
    print('       Seja Muito Bem Vindo(a) ')
    print('                 Ao')
    print('     Nosso Sistema de Criptomoeda!')
    time.sleep(0.2)

    #Except -------------------------------------
    def erro():
        print('Tente colocar um numero inteiro na proxima!')
        fechando = 'Fechando o sistema...'
        for letra in fechando:
            print('\033[31m' + letra + '\033[m', end='', flush=True)
            time.sleep(0.1)
        exit()
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

        print('\033[34m-=\033[m'*20)
        print('Oque você deseja fazer nesse sistema?')
        print('[ 1 ] - Minerar')
        print('[ 2 ] - Transferir')
        print('[ 3 ] - Ver Saldo')
        print('[ 0 ] - Sair!!')
        print('\033[34m-=\033[m'*20)
        try:
            op = int(input('Opção: '))
        except:
            erro()
            
        if op == 0:
            print('Tchau, Tchau', end='')
            for _ in range(3):
                print('.', end='', flush=True)
                sleep(0.8)
            print()
            exit()

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
                nomeTranferência = str(input('Nome: '))
                valor_transferencia = float(input('Valor: R$'))

                find_arq = os.path.isfile('Discripto.txt')

                if find_arq == True:

                    print('\033[34m-=\033[m'*25)
                    print('Você tem certeza que quer continuar?')
                    print('[ 1 ] - Sim')
                    print('[ 2 ] - Não')
                    print('\033[34m-=\033[m'*25)

                    try:
                        op = int(input('Opção: '))
                    except:
                        erro()

                    if op == 1:
                        with open('Discripto.txt', 'r') as arquivo_descriptografado:
                            dinheiro = arquivo_descriptografado.read()
                        
                        # money = dinheiro
                        money_convert = float(dinheiro)

                        if money_convert - valor_transferencia >= 0:
                            with open('Discripto.txt', 'w') as arquivo_descriptografado:
                                arquivo_descriptografado.write(f'{money_convert - valor_transferencia}')

                            correto = '\033[32mOk. Transação feita com sucesso\033[m'
                            for letra in correto:
                                print(letra, end='', flush=True)
                                time.sleep(0.09)
                            print()
                            break
                        else:
                            print(f'A transação não pôde ser completada.\nVocê tem apenas R${money_convert} para fazer uma transação de R${valor_transferencia}!!')
                            break

                    elif op == 2:
                        print('\033[34m-=\033[m'*25)
                        print('Cancelando Transação', end='')
                        for _ in range(3):
                            print('.', end='', flush=True)
                            time.sleep(0.3)
                        print('')
                        break

                    else:
                        print('\033[34m-=\033[m'*25)
                        invalida = '\033[31mAlternativa inválida!\033[m'
                        for letra in invalida:
                            print(letra, end='', flush=True)
                            time.sleep(0.09)
                        print()

                else:
                    print('\033[34m-=\033[m'*25)
                    inexistente = '\033[31mO arquivo "Discripto.txt" não foi encontrado\033[m'
                    for letra in inexistente:
                        print(letra, end='', flush=True)
                        time.sleep(0.09)
                    print()
                    retente = '\033[31mTente minerar primeiro\033[m'
                    for letra in retente:
                        print(letra, end='', flush=True)
                        time.sleep(0.09)
                    print()
                    break
                    

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
        else:
            print('\033[31mEssa alternativa não existe tente novamente!\033[m')
except:
    print('\nO sistema está fechando pós um erro!')