from random import randint

def function():
    number = randint(0, 100)
    tent = 0
    print('-=-'*15)
    print('Acerte o numero atualizado!!')
    print('-=-'*15)

    while tent <= 10:
        question = int(input('Digite um numero de "0" à "100": '))
        tent += 1

        if question > 100 or question < 0:
            print(f'{question} Não se encaixa no padrão. Tente novamente!!')
            tent -= 1
        
        elif question > number:
            print(f'{question} é maior que o numero secreto. Tente novamente!!')

        elif question < number:
            print(f'{question} é menor que o numero secreto. Tente novamente!!')

        else:
            print(f'Você acertou o numero secreto. Parabéns!!!')
            return
    else:
        print(f'Suas Tentativas acabaram. O numero secreto era {number}')

function()
    