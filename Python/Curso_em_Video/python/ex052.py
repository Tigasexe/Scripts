n = int(input('Digite um numero: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')

if t <= 2:
    print('\n{} é divisível por {} numeros por tanto É PRIMO!'.format(n, t))
else:
    print('\n{} é divisível por {} numeros por tanto NÃO PRIMO!'.format(n, t))