from Pessoa import *
from Aluno import *
class Diretor(Pessoa, Aluno):
    def __init__(self,nome, idade, cpf, cargo):
        super().__init__(nome, idade, cpf, cargo)
        self.adicionarAluno()
        

    def adicionarAluno(self):
        self.diretor= Pessoa('João', 35,'333.333.333-33', 'Diretor')
        print('')
        print('Adicionar Aluno')
        self.aluno= Aluno()



    def __str__(self):
        return f'Diretor: {self.diretor}, \nAluno adicionado: {self.aluno}'
    


