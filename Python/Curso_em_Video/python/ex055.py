maiorPeso = 0
menorPeso = 0

for c in range(1, 5 + 1):
    peso = float(input('Peso da {}º Pessoas: '.format(c)))

    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if menorPeso > peso:
            menorPeso = peso


print('O maior peso lido foi {}'.format(maiorPeso))
print('O menor peso lido foi {}'.format(menorPeso))