class Carros():

    def __init__(self, marca, modelo, velocidade_max):
        #observar os atributos que variam para colocá-los como parametro.
        self.marca = marca
        self.modelo = modelo
        self.velocidade_max = velocidade_max
        self.ligado = False
        self.velocidade_atual = 0

    def ligar(sewlf):

        if not self.ligado and self.velocidade_atual == 0:
            self.ligado = True

        else:
            raise ValueError('O carro já está ligado ou o carro não está parado!')

    def desligar(self):
        if not self.ligado:
            raise ValueError("O carro está parado!")
        elif self.velocidade_atual > 0:
            raise ValueError("O carro não está parado!")
        self.ligado = False

    def acelerar(self):

        if not self.ligado:
            raise ValueError("O carro está desligado!")

        elif self.velocidade_atual >= self.velocidade_max:
            raise ValueError("O carro já está na velocidade máxima!")
        self.velocidade_atual += 5
        #O "5" é que o carro vai acelerar de 5 em 5 toda vez q o motorista pisar no acelerador.


    def frear(self):

        if not self.ligado:
            raise ValueError("O carro está desligado!")

        elif self.velocidade_atual == 0:
            raise ValueError("O carro já está parado!")
        #Não precisa do else pq o cód só chega na última linha se as condições acima forem falsas.
        self.velocidade_atual -= 5