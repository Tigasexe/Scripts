f = str(input('Digite uma palavra: ')).lower()
fr = f[::-1]
print('{} ao contrário é {}'.format(f, fr))

if f == fr:
    print('{} é uma palavra políndromo'.format(f))
else:
    print('{} NÃO é uma palavra políndromo'.format(f))