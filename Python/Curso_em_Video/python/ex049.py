n = int(input('Digite um número para ver a sua tabuada: '))
for t in range(1, 10 + 1):
    print('{} x {} = {}'.format(n, t, n * t))