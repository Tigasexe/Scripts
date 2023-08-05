from carros import Carros

onix = Carros('GM','Onix', 230)
try:
    onix.ligar()
    print('O carro já está ligado!')
    onix.ligar()
    print('O carro já está ligado!')
except ValueError as erro:
    print(erro)
onix.acelerar()