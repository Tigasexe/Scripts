print('Gerador de PA')
print('-=-'*5)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
parada = 0
termos = 0
print('{}'.format(pt), end=' ➛ ')
while parada < 9:
    print('{}'.format(pt + r), end= ' ➛ ')
    parada += 1 
    pt = pt + r
    termos += 1
while True:
    print('PAUSA')
    pr = int(input('Quantos termos você quer mostrar a mais? '))
    parada2 = 0
    if pr == 0:
        print('Progressão finalizada com {} termos mostrados.'.format(termos + 1))
        break
    while parada2 < pr:
        print('{}'.format(pt + r), end=' ➛ ')
        pt = pt + r
        parada2 += 1
        termos += 1