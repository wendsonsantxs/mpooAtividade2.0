class Pessoa():
    def __init__(self, nome, idade, cpf, cargo):
        self.idade= idade
        self.nome=nome
        self.cpf= cpf
        self.cargo= cargo
    

    def __str__(self):
        return f'Nome:{self.nome}, Idade: {self.idade}, Cpf: {self.cpf} \nCargo{self.cargo}'

