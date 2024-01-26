#kW


ValorKW = (750 / 10) / 10

while True:
    try:
        print('Qual o valor que veio no seu ultimo papel de energia?')
        valorGasto = float(input('R$: '))
    except:
        print('Ouve um erro! Por favor tente Novamente.')
        continue
    def KW():
        global kw
        kw = valorGasto / (ValorKW / 10)
    KW()
    print(f'O valor de KW cobrado pelo ultimo papel de energia foi {kw:.2f}kW')
    
    continua = str(input('Quer continuar "S" para Sim ou "N" para Não: '))

    if continua.lower() == 's':
        continue
    else:
        print('Tchau...')
        break

    