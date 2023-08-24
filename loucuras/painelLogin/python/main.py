#Sistema de Criptomoeda! -----------------------------------
import time

print('\033[33m-=\033[m'*15)
print('   Seja Muito Bem Vindo(a) ')
print('             Ao')
print(' Nosso Sistema de Mineração!')
print('\033[33m-=\033[m'*15)

ia = 'Luiz'

frase1 = f'{ia}: Olá me chamo {ia} eu sou a inteligencia artificial do sistema de mineração'
for letra in frase1:
    print(letra, end='', flush=True)
    time.sleep(0.03)

#Conversação -----------------------------------
nome = str(input(f'\n{ia}: Qual o seu nome? ')).strip()

if nome.lower() == 'luiz':
    conv1 = f'{ia}: Nossa que nome bonito hehe!'
    for letra in conv1:
        print(letra, end='', flush=True)
        time.sleep(0.03)
elif nome.lower() == 'luis':
    conv1 = f'{ia}: Por causa de uma letra seu nome não é igual ao meu, rsrs!'
    for letra in conv1:
        print(letra, end='', flush=True)
        time.sleep(0.03)
else:
    conv1 = f'{ia}: É um prazer conhecer você {nome}'
    for letra in conv1:
        print(letra, end='', flush=True)
        time.sleep(0.03)

#Escola! -----------------------------------



#Sistema de Mineração! -----------------------------------



