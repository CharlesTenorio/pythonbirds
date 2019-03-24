"""
Você deve crai um classe carro qeu vai possuir dois aributos compostos por outras duas classeses:
1) Motor
2) Direção

o Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado Velocidade
2 Método acelerar, que deverá incrementar a velocidade de uma unidade
3 Método frea que deverá decrementar a velocidade em duas unidade

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes
atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar a direita
2) Método girar a esquerda

    N
O       L
    S

Exemplo:
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
1
>>> motor.acelerar()
2
>>> motor.acelerar()
3
>>> motor.frear()
1
>>> #Testando Direcao

>>> direcao = Direcao()
>>> direcao.valor
 'Norte'
>>> direcao.girar_a_direita('direita')
 'Leste'

>>> direcao.girar_a_direita('direita')
 'Sul'

>>> direcao.girar_a_direita('direita')
 'Oeste'

>>> direcao.girar_a_direita('direita')
 'Norte'

>>> direcao.girar_a_esquerda('esquerda')
 'Oeste'

>>> direcao.girar_a_esquerda('esquerda')
 'Oeste'

>>> direcao.girar_a_esquerda('esquerda')
 'Sul'

>>> direcao.girar_a_esquerda('esquerda')
 'Leste'

>>> direcao.girar_a_esquerda('esquerda')
 'Norte'

>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2

>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
>>> 'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
>>> 'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calular_direcao()
>>> 'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
>>> 'Oeste'
"""
class Motor:
   def __init__(self):
       self.velocidade = 0

   def acelerar(self):
       self.velocidade +=1

   def frear(self):
       self.velocidade -=2
       self.velocidade = max(0, self.velocidade)


NORTE ='Norte'
SUL = 'Leste'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    rota_direita_dct = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
    rota_esquerda_dct = {NORTE:OESTE, LESTE:NORTE, SUL:LESTE, OESTE:SUL}
    def __init__(self):
        self.valor= NORTE

    def girar_a_direita(self):
        self.valor = self.rota_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rota_esquerda_dct(self.valor)

    def calcular_direcao(self, posicao_atual, direcao):
        if direcao=='direita' and posicao_atual=='Norte':
            self.valor = 'Leste'

        elif  direcao=='direita' and posicao_atual=='Leste':
            self.valor = 'Sul'

        elif direcao == 'direita' and posicao_atual == 'Sul':
            self.valor = 'Oeste'

        elif direcao == 'direita' and posicao_atual == 'Oeste':
            self.valor = 'Norte'

        # a esquerda #
        if direcao=='esquerda' and posicao_atual=='Norte':
            self.valor = 'Oeste'

        elif  direcao=='esquerda' and posicao_atual=='Oeste':
            self.valor = 'Sul'

        elif direcao == 'esquerda' and posicao_atual == 'Sul':
            self.valor = 'Leste'

        elif direcao == 'esquerda' and posicao_atual == 'Leste':
            self.valor = 'Norte'


        return self.valor


class Carro(Motor, Direcao):

    Motor.acelerar()
    Motor.frear()
    Direcao.girar_a_direita('direita')
    Direcao.girar_a_esquerda('esquerda')
