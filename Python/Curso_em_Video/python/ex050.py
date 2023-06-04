i = 0
s = 0
for c in range(1, 6 + 1):
    n = int(input('Digite o {}º Número: '.format(c)))
    if n % 2 == 0:
        i += 1
        s += n
print('Tem {} Números pares e a soma entre eles é de {}'.format(i, s))