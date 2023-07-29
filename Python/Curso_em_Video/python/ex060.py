from math import factorial
print('Digite um numero para')
numero = int(input('calcular seu Fatorial:'))
c = numero

print('Calculando {}! = '.format(numero), end=' ')
while c > 0:
    if c == 1:
        print('{} = {}'.format(c, factorial(numero)))
        break
    print('{} x'.format(c), end=' ')
    c -= 1