#1 - Faça uma piramide em ordem crescente com o valor de N. 
#E se o numero for menor que 0 não entre na piramide!!


print('***'*4)
print('Piramides')
print('***'*4)

num = int(input('Digite um numero: '))
print('[ 1 ] Para crescente')
print('[ 2 ] Para decrescente')
p = int(input('Escolha uma opção: '))

while p != 1 and p != 2:
    print(f'{p} É uma opção invalida. Tente novamente!!')
    p = int(input('Escolha uma opção: '))

if p == 1:
    cont = 1
    while cont <= num:
        cont2 = cont
        while cont2 <= num:
            print(cont2, end=' ')
            cont2 += 1
        print()
        cont += 1

elif p == 2:
    cont = num
    while cont >= 1:
        cont2 = cont
        while cont2 >= 1:
            print(cont2, end=' ')
            cont2 -= 1
        print()
        cont -= 1


