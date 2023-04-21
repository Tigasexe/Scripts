'''#Leia o sexo de uma pessoa, mas, só aceite os valores M ou F


nome = str(input('Qual o seu nome: '))
sexo = str(input('Qual o seu sexo digite "M" para masculino ou "F" para feminino: '))

#Enquanto
while sexo != 'M' and sexo != 'm' and sexo != 'F' and sexo != 'f':
    print('Dado invalido. Tente Novamente!')
    sexo = str(input('Qual o seu sexo digite "M" para masculino ou "F" para feminino: '))

if sexo == 'M' or sexo == 'm':
    print('É um prazer senhor', nome)
elif sexo == 'F' or sexo == 'f':
    print('É um prazer senhora', nome)






#While é quando estiver em naquela condição vai entrar alí'''


'''num = int(input('Digite um numero: '))
cont = 1

while cont <= 10:
    print(num, 'x', cont, '=', num * cont)
    cont += 1'''

#piramide------
'''num = int(input('Digite um numero: '))
linha = num

while linha >= 1:
    coluna = linha
    while coluna >= 1:
        print(coluna, end=' ')
        coluna -= 1
    print()
    linha -= 1
    
# 10 9 8 7 6 5 4 3 2 1
# 9 8 7 6 5 4 3 2 1
# 8 7 6 5 4 3 2 1
# 7 6 5 4 3 2 1
# 6 5 4 3 2 1
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1'''


