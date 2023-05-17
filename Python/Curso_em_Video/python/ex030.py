n = int(input('Me diga um numero: '))

if n % 2 == 0:
    print('O numero {} é \033[34mPAR\033[m'.format(n))
else:
    print('O numero {} é \033[34mIMPAR\033[m'.format(n))