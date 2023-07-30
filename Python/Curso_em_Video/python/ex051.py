print('='*15)
print('{:^15}'.format('10 TERMOS DE UMA PA'))
print('='*15)

pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
decimo = pt + (10 -1) * r

for c in range(pt, decimo, r):
    print(c, end=' ➛ ')

print('ACABOU!')