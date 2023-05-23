print('{:=^50}'.format('LOJA IZAIAS'))
preço = float(input('Preço das Compras: R$'))
print('[ 1 ] à Vista dinheiro')
print('[ 2 ] à Vista Cartão')
print('[ 3 ] 2x no Cartão')
print('[ 4 ] 3x ou mais no Cartão')
op = int(input('Qual é a Opção? '))

if op == 1:
    d = preço - (preço * (10 / 100))
    print('O preço que era {} ficará {}'.format(preço, d))
elif op == 2:
    d = preço - (preço * (5 / 100))
    print('O preço que era {} ficará {}'.format(preço, d))
elif op == 3:
    print('O Preço Ficará {}'.format(preço))
elif op == 4:
    j = preço + (preço * (20 / 100))
    parcela = int(input('Quantas Parcelas? '))
    print('Sua Compra Será Parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, j / parcela))
    print('Sua Compra de R${:.2f} Vai Custar R${:.2f} No Final.'.format(preço, j))