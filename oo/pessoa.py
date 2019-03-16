class Pessoa:
    def __init__(self, *filhos,  nome=None, idade=44):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
       return f'olá{id(self)}'

if __name__== '__main__':
   caua = Pessoa(nome='Paulo')
   charles = Pessoa(caua, nome='Charles')
   print(Pessoa.cumprimentar(charles))
   print(id(charles))
   print(charles.cumprimentar())
   print (charles.nome)
   print(charles.idade)
   for filho in charles.filhos:
       print(filho.nome)

   charles.sobrenome = 'Tenorio'
   del charles.idade
   print(charles.__dict__)
   print(caua.__dict__)