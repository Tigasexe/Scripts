maioridadem = 0
somaidade = 0
nomevelho = ''
mulheres = 0
menorde20 = 0

for c in range(4):
    print('----- {}º Pessoa -----'.format(c + 1))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaidade += idade
    
    if sexo.lower() == 'm':
        if idade > maioridadem:
            nomevelho = nome
            maioridadem = idade
    elif sexo.lower() == 'f':
        if idade < 20:
            menorde20 += 1

print('A media de idade do grupo é {}'.format(somaidade / 4))
print('O homem mais velhor tem {} anos e se chama {}'.format(maioridadem, nomevelho)) 
print('Ao todo são {} mulheres menores de 20 anos'.format(menorde20))
