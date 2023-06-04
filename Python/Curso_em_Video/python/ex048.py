n = 0
s = 0
for c in range(1, 501, 2):
        if c % 3 == 0:
            s += c
            n += 1
print('A soma de Todos os {} numeros é {}'.format(n, s))