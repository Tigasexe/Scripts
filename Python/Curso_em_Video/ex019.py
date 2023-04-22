from random import choice
primeiro_aluno = str(input('Primeiro Aluno: '))
segundo_aluno = str(input('Segundo Aluno: '))
terceiro_aluno = str(input('Terceiro Aluno: '))
quarto_aluno = str(input('Quarto Aluno: '))
alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
aluno_escolhido = choice(alunos)
print('O aluno(a) escolhido(a) foi {}'.format(aluno_escolhido))