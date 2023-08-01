opcao = ''
while opcao != '06':
    print('=============================')
    print('| 01 - Resolução questão 01 |')
    print('| 02 - Resolução questão 02 |')
    print('| 03 - Resolução questão 03 |')
    print('| 04 - Resolução questão 04 |')
    print('| 05 - Resolução questão 05 |')
    print('| 06 - Sair do Sistema      |')
    print('=============================')
    opcao = int(input("Digite sua escolha aqui: "))
    if opcao == 1:
        print ('Questão 01:')
        gabarito = ['', '', '', '', '', '', '', '', '', '']
        iago = ['', '', '', '', '', '', '', '', '', '']
        cont = 0
        for i in range(10):
            gabarito[i] = input("Digite a alternativa correta no gabarito: ")
        for j in range(10):
            iago[j] = input("Digite a alternativa marcada por iago: ")
            if iago[j] == gabarito[j]:
                cont += 1
        print("Iago acertou", cont, 'de', len(gabarito), 'questões.')
    elif opcao == 2:
        print('Questão 02:')
        sair = ''
        cont = 0
        nome = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        altura = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sexo = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        while sair != "sim" and cont < 5:
            nome[cont] = input('Digite o nome da pessoa: ')
            altura[cont] = float(input("Digite a altura da pessoa em cm. Ex: 190 cm: "))
            S = int(input("Digite o sexo da pessoas (0 para masculino, 1 para feminino): "))
            if S == 1:
                sexo[cont] = 'Feminino'
            else:
                sexo[cont] = 'Masculino'
            cont += 1
            sair = str(input('Deseja sair?(sim/não): '))
        maior = -1
        menor = 5000
        maior_id = ''
        menor_id = ''
        for k in range(cont):
            if altura[k] > maior:
                maior = altura[k]
                maior_id = k
            if altura[k] < menor:
                menor = altura[k]
                menor_id = k
        print('\nA maior altura foi de', altura[maior_id], 'cm, sendo da pessoa', nome[maior_id], 'de sexo',
              sexo[maior_id])
        print('A menor altura foi de', altura[menor_id], 'cm, sendo da pessoa', nome[menor_id], 'de sexo',
              sexo[menor_id])
        pop_altura = 0
        soma_Mulher = 0
        quant_mulher = 0
        media = 0
        for i in range(cont):
            pop_altura += altura[i]
            if sexo[i] == 'Feminino':
                soma_Mulher += altura[i]
                quant_mulher += 1
        if quant_mulher > 0:
            media = soma_Mulher / quant_mulher
        print('A média de altura das mulheres é', media , 'cm')
        print('A média da altura da população é', pop_altura / cont, 'cm')
        per_masc = 0
        for j in range(cont):
            if sexo[j] == 'Masculino':
                per_masc += 1
        print('A quantidade média de Homens foi de', (per_masc / cont) * 100, '%')
    elif opcao == 3:
        print('Questão 03:')
        num = int(input('Digite um numero: '))
        if num <= 0:
            print('Número Invalido')
        else:
            print('Divisores de', num, ':\n')

            for c in range(num,0,-1):
                if num % c == 0:
                    print(c)
    elif opcao == 4:
        print('Questão 04:')
        maior = -9999999999999999999999
        menor = 9999999999999999999999
        for i in range(10):
            num = int(input("Digite um numero: "))
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        print("Maior numero inserido:", maior)
        print("Menor numero inserido:", menor)
    elif opcao == 5:
        print('Questão 05:')
        palavra = ""
        cont = -1
        while len(palavra) < 5 or cont != 0:
            palavra = input("Digite uma palavra: ")
            if len(palavra) < 5:
                print("A palavra precisa ter pelo menos 5 caracteres.")
            else:
                cont = 0
                for i in range(len(palavra)):
                    if palavra[i] != palavra[-(i + 1)]:
                        cont += 1
                if cont > 0:
                    print("A palavra não é um palíndromo.")

        print("A palavra", palavra, "é um palíndromo!")
    elif opcao == 6:
        print ("Programa encerrado!")
        break
    else:
        print ('Você informou uma opção inválida. Preste atenção ao menu de opções.')