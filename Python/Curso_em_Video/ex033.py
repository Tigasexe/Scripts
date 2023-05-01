n1 = int(input('Digite o primeiro valor: ')) 
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
maior = 0
meio = 0
menor = 0

if n1 > n2 and n1 > n3:
    maior = n1
    meio = n2
    if n3 > n2 and n3 < n1:
        meio = n3
    menor = n2
    if n3 < n2 and n3 < n1:
        menor = n3
elif n2 > n1 and n2 > n3:
    maior = n2
    meio = n1
    if n3 > n1 and n3 < n2:
        meio = n3
    menor = n1
    if n3 < n1 and n3 < n2:
        menor = n3
elif n3 > n1 and n3 > n2:
    maior = n3
    meio = n2
    if n1 > n2 and n1 < n3:
        meio = n1
    menor = n2
    if n1 < n2 and n1 < n3:
        menor = n1

print('O maior numero é {}'.format(maior))
print('O numero do meio é {}'.format(meio))
print('O menor numero é {}'.format(menor))