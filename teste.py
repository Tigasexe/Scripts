import string
import random
import hashlib
import time

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

cripto1 = hashlib.sha256(code1.encode()).hexdigest()
cripto2 = hashlib.sha256(code2.encode()).hexdigest()
cripto3 = hashlib.sha256(code3.encode()).hexdigest()
cripto4 = hashlib.sha256(code4.encode()).hexdigest()
cripto5 = hashlib.sha256(code5.encode()).hexdigest()
cripto6 = hashlib.sha256(code6.encode()).hexdigest()
cripto7 = hashlib.sha256(code7.encode()).hexdigest()
cripto8 = hashlib.sha256(code8.encode()).hexdigest()
cripto9 = hashlib.sha256(code9.encode()).hexdigest()
cripto10 = hashlib.sha256(code10.encode()).hexdigest()

criptos = [cripto1, cripto2, cripto3, cripto4, cripto5, cripto6, cripto7, cripto8, cripto9, cripto10]
chaves = [cripto1, cripto2, cripto3, cripto4, cripto5, cripto6, cripto7, cripto8, cripto9, cripto10]

def gerador_de_senhas(tamanho):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for c in range(tamanho))

def sha256_hash(texto):
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()

tamanho_chave = 64
tentativas = 0

for _ in range(600):
    chave_random = gerador_de_senhas(tamanho_chave)
    chave_hashed = sha256_hash(chave_random)
    chaves.append(chave_hashed)

while True:
    escolha = random.randint(0, 609)

    if chaves[escolha] in criptos:
        print(f'\033[32m{chaves[escolha]}\033[m')
        time.sleep(0.1)
        break
    else:
        print(f'\033[31m{chaves[escolha]}\033[m')
        time.sleep(0.1)

print('Chave Encontrada!')