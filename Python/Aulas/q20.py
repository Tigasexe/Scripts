opção = 0
soma = 0
subtrair = 0
multiplicar = 0
dividir = 0
exponenciar = 0

while opção != 6:

    print('[ 1 ] Somar')
    print('[ 2 ] Subtrair')
    print('[ 3 ] Multiplicar')
    print('[ 4 ] Dividir')
    print('[ 5 ] Exponenciar')
    print('[ 6 ] Encerrar')
    opção = int(input('Opção: '))

    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o primeiro valor: '))

    if opção == 1:
        soma = v1 + v2
        print(soma)

    elif opção == 2:
        subtrair = v1 - v2
        print(subtrair)

    elif opção == 3:
        multiplicar = v1 * v2
        print(multiplicar)

    elif opção == 4:
        dividir = v1 / v2
        print(dividir)

    elif opção == 5:
        exponenciar = v1 ** v2
        print(exponenciar)
