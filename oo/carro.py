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
>>> direcao.girar_a_direita()
 'Leste'

>>> direcao.girar_a_direita()
 'Sul'

>>> direcao.girar_a_direita()
 'Oeste'

>>> direcao.girar_a_direita()
 'Norte'

>>> direcao.girar_a_esquerda()
 'Oeste'

>>> direcao.girar_a_esquerda()
 'Oeste'

>>> direcao.girar_a_esquerda()
 'Sul'

>>> direcao.girar_a_esquerda()
 'Leste'

>>> direcao.girar_a_esquerda()
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