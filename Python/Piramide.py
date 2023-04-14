n = int(input('Escolha um numero: '))

for c in range(n + 1):
    for p in range(c):
        print(p, end=' ')
    print()