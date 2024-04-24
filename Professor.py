from Endereco import *
from Disicplina import *
class Professor(Endereco, Disciplinas):
    def __init__(self):
        self.adicionarProfessor()

    def adicionarProfessor(self):
        
        self.nome= input('Nome:')
        self.cpf= input('Cpf:')
        self.endereco= Endereco()
        self.disciplina = Disciplinas()

    def __str__(self):
        return f'Professor: {self.nome}, \nCpf: {self.cpf}, \nEndereço: {self.endereco}\n{self.disciplina}'

