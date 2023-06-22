print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Cachorro -------------- R$100,00')
print('Gato ------------------ R$100,00')
print('Papagaio -------------- R$150,00')
print('Periquito australiano - R$175,00')
print('Iguana ---------------- R$200,00')
print('Peixe beta ------------ R$50,00')
print('   DIGITE "sair" para parar!! ')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print()

Cachorro = 100.00
Gato = 100.00
Papagaio = 150.00
Periquito = 175.00
Iguana = 200.00
Peixe = 50.00
preço = 0
parar = 0

while parar != 'sair':
    parar = input('Digite o nome do animal que você deseja: ')

    if parar != 'Cachorro' and parar != 'Gato' and parar != 'Papagaio' and parar != 'Periquito australiano' and parar != 'Iguana' and parar != 'Peixe beta' and parar != 'sair':
        print('Animal Não Cadastrado!')

    if parar == 'Cachorro':
        preço += Cachorro

    elif parar == 'Gato':
        preço += Gato

    elif parar == 'Papagaio':
        preço += Papagaio

    elif parar == 'Periquito australiano':
        preço += Periquito
    
    elif parar == 'Iguana':
        preço += Iguana

    elif parar == 'Peixe beta':
        preço += Peixe

print('O valor do carrinho eh', preço)