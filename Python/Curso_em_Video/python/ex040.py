'''
< 5 reprovado
>= 5 and <= 6.9 recuperação
> 7 aprovado
'''

pn = float(input('Primeira Nota: '))
sn = float(input('Segunda Nota: '))
m = (pn + sn) / 2

print('Tirando {} e {}, a média do aluno é {}'.format(pn, sn, m))

if m < 5:
    print('O aluno está REPROVADO')
elif m >= 5 and m <= 6.9:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')
