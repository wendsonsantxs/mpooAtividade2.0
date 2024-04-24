class Endereco():
    def __init__(self):
        self.adicionarAluno()
        

    def adicionarAluno(self):
        self.rua=input('Rua:')
        self.numero= int(input('Numero (apenas numeros):'))
        self.bairro= input('Bairro:')
        self.cep= input('Cep:')

    def __str__(self):
            return f'Rua: {self.rua}, Numero: {self.numero}, Bairro: {self.bairro}, Cep: {self.cep}'




    

