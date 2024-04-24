from Sala import *
from Pessoa import *

class Servidor(Pessoa):
    def __init__(self,nome, idade, cpf, cargo):
        super().__init__(nome, idade, cpf, cargo)
        self.adicionarServidor()
    

    def adicionarServidor(self):
        self.pessoa= Pessoa('Marcos', 40,'111.222.333-44', 'Servidor')
        print('')
        self.sala= Sala()

    def __str__(self):
        return f'Função: Criar sala. \nDados do servidor: {self.pessoa},\n Sala: {self.sala}'
    


