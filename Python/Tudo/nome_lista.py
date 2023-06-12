print('-=-'*15)
print('Para Parar Digite Sair')
print('-=-'*15)

lista_alunos = []
while True:
    alunos = str(input('Digite o nome do aluno: '))
    lista_alunos.append(alunos)
    if alunos.lower() == 'sair':
        break
   
lista_alunos.remove('sair')
print(lista_alunos)
print(f'Na sua sala tem {len(lista_alunos)} Pessoas')