pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))

#---- Variaveis de apoio
somar = pv + sv
multiplicar = pv * sv
maior = 0

while True:
    print('     [ 1 ] somar')
    print('     [ 2 ] multiplicar')
    print('     [ 3 ] maior')
    print('     [ 4 ] novos números')
    print('     [ 5 ] sair do programa')
    op = int(input('>>>>> Qual é a sua opção? '))
    
    if op == 1:
        print('O resultado de {} + {} é {}'.format(pv, sv, somar))
    elif op == 2:
        print('O resultado de {} x {} é {}'.format(pv, sv, multiplicar))
    elif op == 3:
        maior = pv
        if sv > pv:
            maior = pv
        print('Entre {} e {} o maior é {}'.format(pv, sv, maior))
    elif op == 4:
        pv = int(input('Primeiro valor: '))
        sv = int(input('Segundo valor: '))
    else:
        break

print('Tchau, Tchau!')
