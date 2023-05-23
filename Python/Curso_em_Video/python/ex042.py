ps = float(input('Primeiro Segmento: '))
ss = float(input('Segundo Segmento: '))
ts = float(input('Terceiro Segmento: '))

if ps < ss + ts and ss < ps + ts and ts < ps + ss:
    print('Seus Segmentos Formam Um Triângulo', end=' ')

    if ps == ss == ts:
        print('Equilátero')
    elif ps == ss or ss == ts or ps == ts:
        print('Isóceles')
    else:
        print('Escaleno')
else:
    print('Os Segmentos Acima Não Formam Um Triângulo!!')