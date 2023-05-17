#Valor menor de 200 é 50R$ == 200 ou maior 45R$

d = float(input('Qual a distância da sua viagem? (km) '))
print('Vocês está prestes a começar uma viagem de {}km.'.format(d))

if d < 200:
    p = d * 0.50
    print('E o preço da sua passagem será {}R$'.format(p))
else:
    p = d * 0.45
    print('E o preço da sua passagem será {}R$'.format(p))