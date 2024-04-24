from Curso import *
from Endereco import *
from Disicplina import *
class Aluno(Curso, Endereco, Disciplinas):
    def __init__(self):
        self.nome= None
        self.matricula= None
        self.adicionarAlunos()

    def adicionarAlunos(self):
        self.nome= input('Nome:')
        self.matricula= input('Matricula (apenas numeros):')
        self.curso= Curso()
        self.endereco= Endereco()
        self.disciplina= Disciplinas()

    def __str__(self):
        return f'Nome: {self.nome}, Matricula:{self.matricula} \n Endereço: {self.endereco}, \n {self.curso}, {self.disciplina}'
