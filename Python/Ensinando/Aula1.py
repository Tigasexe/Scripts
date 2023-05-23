#Faça Um Script Que peças informações do tipo:
# -> Nome
# -> Data de Nascimento
# E com essas informações forneça a idade do usuario;
# Ex: "Nome Do Usuaria" Você Nasceu em "Data de Nascimento" e Você tem "Idade" anos

from datetime import date

ano =int(input("em que ano você: "))
nome = input("coloque seu nome: ")
anoAtual = date.today().year
idade = anoAtual - ano
print ("olá", nome, "você nasceu em", ano, "você tem", idade)

if idade >= 18:
    print("você é de maior")
elif idade > 15 and idade < 17:
    print("você está prestes a se alistar no exercito")