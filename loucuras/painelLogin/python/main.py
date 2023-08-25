#Bibliotecas importadas ----------------------------------

from hashlib import sha256 #Criptografia
from time import sleep #Tempo
import string #Criar strings
import time #Tempo
import random #Randomizar Senha
import hashlib #Criptografia

'''#Boas Vindas -----------------------------------

print('\033[33m-=\033[m'*15)
print('   Seja Muito Bem Vindo(a) ')
print('             Ao')
print(' Nosso Sistema de Criptomoeda!')
print('\033[33m-=\033[m'*15)
print('')
time.sleep(1)

ia = ''
sexoia = ''

#Sexo IA -----------------------------------

print('\033[33m-=\033[m'*20)
print("Escolha o sexo da sua(seu) Assistente! ") 
print("[ 1 ] - Para Masculino ")
print("[ 2 ] - Para Feminino ")
print('\033[33m-=\033[m'*20)
sexoia = int(input('Opção: '))
print('')

if sexoia == 1:
    print('\033[33m-=\033[m'*20)
    print("Escolha o nome da seu Assistente! ") 
    print("[ 1 ] - Jarvis")
    print("[ 2 ] - Alfred")
    print("[ 3 ] - Louis")
    print("[ 4 ] - Ziggy")
    print('\033[33m-=\033[m'*20)
    nomeia = int(input("Opção: "))
    
    while nomeia != 1 and nomeia != 2 and nomeia != 3 and nomeia != 4:
        print('Alternativa inválida. Tente novamente!!')
        print('\033[33m-=\033[m'*20)
        print("Escolha o nome do seu Assistente!") 
        print("[ 1 ] - Jarvis")
        print("[ 2 ] - Alfred")
        print("[ 3 ] - Louis")
        print("[ 4 ] - Ziggy")
        print('\033[33m-=\033[m'*20)
        nomeia = int(input("Opção: "))

    if nomeia == 1:
        ia = "Jarvis"
    elif nomeia == 2:
        ia = "Alfred"
    elif nomeia == 3:
        ia = "Louis"
    elif nomeia == 4:
        ia = "Ziggy"

elif sexoia == 2:
    print('\033[33m-=\033[m'*20)
    print("Escolha o nome da sua Assistente!") 
    print("[ 1 ] - Aurora")
    print("[ 2 ] - Serena")
    print("[ 3 ] - Athena")
    print("[ 4 ] - Iris")
    print('\033[33m-=\033[m'*20)
    nomeia = int(input("Opção: "))
    
    while nomeia != 1 and nomeia != 2 and nomeia != 3 and nomeia != 4:
        print("Alternativa inválida. Tente novamente!!")
        print('\033[33m-=\033[m'*20)
        print("Escolha o nome da sua Assistente!") 
        print("[ 1 ] - Aurora")
        print("[ 2 ] - Serena")
        print("[ 3 ] - Athena")
        print("[ 4 ] - Iris")
        print('\033[33m-=\033[m'*20)
        nomeia = int(input("Opção: "))

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

nome = str(input(f'\n{ia}: Qual o seu nome? ')).strip()

if nome.lower() == ia.lower():
    conv1 = f'{ia}: Nossa que nome bonito hehe!'
    for letra in conv1:
        print(letra, end='', flush=True)
        time.sleep(0.03)
else:
    conv1 = f'{ia}: É um prazer conhecer você {nome}'
    for letra in conv1:
        print(letra, end='', flush=True)
        time.sleep(0.03)
print('')
'''
#Menu do Sistema -----------------------------------

while True:
    print('\033[34m-=\033[m'*15)
    print('[ 1 ] - Minerar')
    print('[ 2 ] - Ver Saldo')
    print('[ 3 ] - Depositar')
    print('[ 4 ] - Sacar')
    print('[ 5 ] - Transferir')
    print('\033[34m-=\033[m'*15)
    op = int(input('Opção: '))
    
    if op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
        print('Alternativa inválida. Tente novamente!')
    
#Sistema de Mineração -----------------------------------

    elif op == 1:

        print('A mineração começará em...')
        
        '''for cont in range(5, 0, -1):
            print(cont)
            sleep(1)'''
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
            chave_hashed = cripto1

            if chave_hashed == cripto1:
                print('\033[32m' + cripto1 + '\033[m')
                print(f'A chave foi encontrada com {tentativas} tentativas')
                find.append(chave_hashed)
                break
            elif chave_hashed == cripto2:
                print('\033[32m' + cripto2 + '\033[m')
                print(f'A chave foi encontrada com {tentativas} tentativas')
                break
            elif chave_hashed == cripto3:
                print('\033[32m' + cripto3 + '\033[m')
                print(f'A chave foi encontrada com {tentativas} tentativas')
                break
            elif chave_hashed == cripto4:
                print('\033[32m' + cripto4 + '\033[m')
                print(f'A chave foi encontrada com {tentativas} tentativas')
                break
            elif chave_hashed == cripto5:
                print('\033[32m' + crpto5 + '\033[m')
                print(f'A chave foi encontrada com {tentativas} tentativas')
                break
            elif chave_hashed == cripto6:
                print('\033[32m' + cripto6 + '\033[m')
                print(f'A chave foi encontrada com {tentativas} tentativas')
                break
            elif chave_hashed == cripto7:
                print('\033[32m' + cripto7 + '\033[m')
                print(f'A chave foi encontrada com {tentativas} tentativas')
                break
            elif chave_hashed == cripto8:
                print('\033[32m' + cripto8 + '\033[m')
                print(f'A chave foi encontrada com {tentativas} tentativas')
                break
            elif chave_hashed == cripto9:
                print('\033[32m' + cripto9 + '\033[m')
                print(f'A chave foi encontrada com {tentativas} tentativas')
                break
            elif chave_hashed == cripto10:
                print('\033[32m' + cripto10 + '\033[m')
                print(f'A chave foi encontrada com {tentativas} tentativas')
                break
            else:
                print('\033[31m' + chave_hashed + '\033[m')
                sleep(0.1)

        with open('Cripto.txt', 'w') as save:
            save.write(''.join(map(str, find)))
        
