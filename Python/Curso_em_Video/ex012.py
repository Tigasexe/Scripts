p = float(input('Qual é o preço do produto? R$'))
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(p, p - (p * (5 / 100))))