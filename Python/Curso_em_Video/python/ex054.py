from datetime import date

atual = date.today().year
maior = 0
menor = 0

for c in range(1, 7 + 1):
    ano = int(input('Em que ano nasceu a {}º pessoa: '.format(c)))

    if atual - ano >= 18:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))