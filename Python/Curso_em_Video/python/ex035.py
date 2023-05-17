print('-=-'*15)
print('Analizador de Triângulos')
print('-=-'*15)

ps = float(input('Primeiro segmento: '))
ss = float(input('Segundo segmento: '))
ts = float(input('Terceiro segmento: '))

if ps + ss > ts and ts + ps > ss and ts + ss > ps:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
