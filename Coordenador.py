from Pessoa import *
from Professor import *
class Coordenador(Pessoa):
    def __init__(self, nome, idade, cpf, cargo):
        super().__init__(nome, idade, cpf, cargo)
        self.funcao= 'Adicionar Professor'
        self.adicionarProfessor()


    def adicionarProfessor(self):
        self.pessoa= Pessoa('Maria', 50,'111.111.111-11', 'Coordenador')
        print('')
        print('Adicionar professor')
        self.professor= Professor()

    def __str__(self):
        return f'Função: Adicionar professor. \nDados do Coordenador: {self.pessoa} \n Dados do Professor adicionado {self.professor}'
    
