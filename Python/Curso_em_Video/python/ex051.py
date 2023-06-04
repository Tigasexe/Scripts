print('='*15)
print('{:^15}'.format('10 TERMOS DE UMA PA'))
print('='*15)

pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))

for c in range(pt, 10, r):
    print(c, end=' ➛ ')

print('ACABOU!')