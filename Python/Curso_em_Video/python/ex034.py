s = float(input('Qual é o salário do funcionário? R$'))

if s > 1250:
    p = s + (s * (10 / 100))
    print('Quem ganhava R${} passou a ganhar R${:.2f}'.format(s, p))
else:
    p = s + (s * (15 / 100))
    print('Quem ganhava R${} passou a ganhar R${:.2f}'.format(s, p))