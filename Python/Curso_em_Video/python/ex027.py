nc = str(input('Digite o seu nome completo: '))
dnc = nc.split()
print('É um prazer conhece-lo {}'.format(dnc[0]))
print('O seu ultimo nome é {}'.format(dnc[len(dnc)-1]))