from datetime import date

ano = int(input('Que ano quer analizar? Digite "0" para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #Acontece de 4 em 4 anos então o ano tem que ser divisível por 4 e não pode ser divisível por 100 ou terá que ser divisível por 400!
    print('{} É um ano BISSEXTO'.format(ano))
else:
    print('{} Não é um ano BISSEXTO'.format(ano))