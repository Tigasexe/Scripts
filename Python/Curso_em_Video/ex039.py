from datetime import date

n = int(input('Ano de Nascimento: '))
ano = date.today().year
idade = ano - n

print('Quem nasceu em {} tem {} anos em {}'.format(n, idade, ano))

if idade == 18:
    print('Você está no ano do seu Alistamento. Boa Sorte!')
elif idade > 18:
    print('Seu alistamento passou a {} anos'.format(idade - 18))
    print('Você deveria ter se alistado em {}'.format(ano + 18))
else:
    print('Ainda falta {} anos para seu alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format(ano + 18))