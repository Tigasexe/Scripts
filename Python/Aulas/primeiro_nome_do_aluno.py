turma = [[""] * 6 for _ in range(46)]
num_alunos_cadastrados = 0
num_alunos_com_situacao = 0

while True:
    print('-=-'*15)
    print("[ 1 ] Cadastrar Aluno")
    print("[ 2 ] Encontrar Aluno")
    print("[ 3 ] Atualizar Situação dos Alunos")
    print("[ 4 ] Gerar Relatório de Alunos Aprovados")
    print("[ 5 ] Gerar Relatório de Alunos Reprovados")
    print("[ 6 ] Sair")
    print('-=-'*15)

    opcao = input("Opção: ")

    if opcao == "1":
        if num_alunos_cadastrados < 46:
            matricula, nome, cpf, email = input("Matrícula: "), input("Nome: "), input("CPF: "), input("E-mail: ")
            media = float(input("Média: "))
            situacao = "Aprovado" if media >= 70 else "Reprovado"
            turma[num_alunos_cadastrados] = [matricula, nome, cpf, email, media, situacao]
            num_alunos_cadastrados += 1
            print("Aluno cadastrado com sucesso!")

        else:
            print("A turma está cheia. Não é possível cadastrar mais alunos.")

    elif opcao == "2":
        matricula_busca = input("Digite a matrícula do aluno que deseja encontrar: ")
        encontrado = False

        for i in range(num_alunos_cadastrados):
            aluno_atual = turma[i]
            if aluno_atual[0] == matricula_busca:
                print("Dados do Aluno:")
                print(f"Matrícula: {aluno_atual[0]}")
                print(f"Nome: {aluno_atual[1]}")
                print(f"CPF: {aluno_atual[2]}")
                print(f"E-mail: {aluno_atual[3]}")
                print(f"Média: {aluno_atual[4]}")
                print(f"Situação: {aluno_atual[5]}")
                encontrado = True
                break

        if not encontrado:
            print("Aluno não encontrado.")

    elif opcao == "3":
        if num_alunos_com_situacao < num_alunos_cadastrados:
            for i in range(num_alunos_cadastrados):
                aluno_atual = turma[i]
                if aluno_atual[5] == "":
                    aluno_atual[5] = "Aprovado" if aluno_atual[4] >= 70 else "Reprovado"
                    num_alunos_com_situacao += 1
            print("Situação dos alunos atualizada.")
        else:
            print("Todos os alunos já têm situação atribuída.")

    elif opcao == "4":
        print("Relatório de Alunos Aprovados:")
        for i in range(num_alunos_cadastrados):
            aluno_atual = turma[i]
            if aluno_atual[5] == "Aprovado":
                print(f"Matrícula: {aluno_atual[0]} | Nome: {aluno_atual[1]} | Média: {aluno_atual[4]}")

    elif opcao == "5":
        print("Relatório de Alunos Reprovados:")
        for i in range(num_alunos_cadastrados):
            aluno_atual = turma[i]
            if aluno_atual[5] == "Reprovado":
                print(f"Matrícula: {aluno_atual[0]} | Nome: {aluno_atual[1]} | Média: {aluno_atual[4]}")

    elif opcao == "6":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1/2/3/4/5/6).")



