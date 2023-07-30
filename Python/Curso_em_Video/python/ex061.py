print('Gerador de PA')
print('-=-'*5)

pt = int(input('Primeira termo: '))
r = int(input('Razão da PA: '))
parada = 0
print('{}'.format(pt), end=' ➛ ')
while parada < 9:
    print('{}'.format(pt + r), end=' ➛ ')
    parada += 1
    pt = pt + r
print('FIM')