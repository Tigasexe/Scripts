v = int(input('Qual é a velocidade atual do carro? (Apenas Numeros) '))

if v > 80:
    print('\033[31mMULTADO! Você excedeu o limite da via (80km/h)')
    print('Você deverá Pagar {}R$ de Multa!'.format((v - 80) * 7))
print('\033[33mTenha Uma Boa Viagem! Dirija com Segurança!\033[m')