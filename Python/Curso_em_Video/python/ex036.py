v = float(input('Valor da Casa: R$'))
s = float(input('Salário do Comprador: R$'))
t = int(input('Quantos Anos de Financiamento? '))
p = v / (t * 12)
sm = s * (30 / 100)

print('Para Pagar uma casa de R${} em {} anos'.format(v, t))
print('As prestações em {} anos será de R${:.2f}'.format(t, p))

if p > sm:
    print('Empréstimo NÃO pode ser CONCEDIDO!')
else:
    print('Empréstimo PODE ser CONCEDIDO!')
