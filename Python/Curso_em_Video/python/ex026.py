p = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase.'.format(p.count('a')))
print('A primeira letra A aparece na {}º posição'.format(p.find('a')+1))
print('A ultima letra A aparece na {}º posição'.format(p.rfind('a')+1))