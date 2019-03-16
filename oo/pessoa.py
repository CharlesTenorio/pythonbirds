class Pessoa:
    olhos = 3
    def __init__(self, *filhos,  nome=None, idade=44):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
       return f'olá{id(self)}'

    @staticmethod
    def metodo_estatico():
        return 44

    @classmethod
    def metodo_da_classe(cls):
        return f'{cls} - {cls.olhos}'

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


   charles.sobrenome = 'Tenorio da Silva'
   del charles.idade
   charles.olhos =1
   del charles.olhos
   print(charles.__dict__)
   print(caua.__dict__)
   print(Pessoa.olhos)
   print(charles.olhos)
   print(caua.olhos)
   print(id(Pessoa.olhos), id(caua.olhos), id(charles.olhos))
   print(Pessoa.metodo_estatico(), caua.metodo_estatico())
   print(Pessoa.metodo_da_classe(), caua.metodo_da_classe())