#Escreva um algoritmo que leia valores inteiros entre -1000 e 1000 e 
#encontre o maior e o menor deles. Termine a leitura se o usuario digitar 0


print('———'*15)
print('     Digite numeros entre -1000 e 1000')
print('           DIGITE "0" PARA PARAR')
print('———'*15)



n1 = int(input('Digite um numero: '))

if n1 == 0 or n1 < -1000 or n1 > 1000:
    print(f'{n1} não está dentro dos padrões')

elif n1 != 0 or n1 > -1000 and n1 < 1000:
    n2 = int(input('Digite outro numero: '))
    
    if n2 == 0 or n2 < -1000 or n2 > 1000:
        print(f'{n2} não está dentro dos padrões')
        
    elif n2 != 0 or n2 > -1000 and n2 < 1000:
        n3 = int(input('Digite outro numero: '))

        if n3 == 0 or n3 < -1000 or n3 > 1000:
            print(f'{n3} não está dentro dos padrões')

        else:
            maior = n1
            if n2 > n3 and n2 > n1:
                maior = n2
            elif n3 > n1 and n3 > n2:
                maior = n3

            menor = n1
            if n2 < n3 and n2 < n1:
                maior = n2
            elif n3 < n1 and n3 < n2:
                maior = n3

            print(f'O maior é {maior} e o menor é {menor}')



