peso = float(input('Qual o Seu Peso? (Kg) '))
altura = float(input('Qual a Sua Altura? (M) '))
imc = peso / (altura ** 2)
print('O IMC Dessa Pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no Peso Ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso!!')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE!!!')
else:
    print('Você está com OBESIDADE MÓRBIDA!!!!')


