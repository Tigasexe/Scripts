from datetime import date

anoAtual = date.today().year
anoNascimento = int(input("Ano do Nascimento: "))
idade = anoAtual - anoNascimento

print('O atleta tem {} anos Portanto'.format(idade))

if idade <= 9:
    print('Classificação MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação JUNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')

