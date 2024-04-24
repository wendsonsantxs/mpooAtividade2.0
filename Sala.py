class Sala():
    def __init__(self):
        nome = input('Sala:')
        capacidade = int(input('Capacidade (apenas numeros):'))
        self.setNome(nome)
        self.setCapacidade(capacidade)



    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome= nome

    def getCapacidade(self):
        return self.__capacidade
    
    def setCapacidade(self, capacidade):
        self.__capacidade= capacidade

    def __str__(self):
        return f'Sala:{self.getNome()} \nCapacidade: {self.getCapacidade()}'



    
    


    
