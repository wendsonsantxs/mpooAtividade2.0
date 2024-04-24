from Diretor import *
from Coordenador import *
from Servidor import *
class Main(Diretor, Coordenador, Servidor):
    def __init__(self):
        self.menu()

    def menu(self):
        print('-*-*- Menu de Opções -*-*-')
        print('Funções: \nCoordenador é adicionar professor \nServidor é criar sala \nDiretor é adicionar aluno')
        print('')
        print('1- Adicionar aluno')
        print('2- Adicionar professor')
        print('3- Criar sala')
        print('4- Sair')
        opcao= int(input('Qual sua escolha?'))
        if (opcao==1):
            self.escolha= Diretor('João', 35,'333.333.333-33', 'Diretor')
        elif (opcao==2):
            self.escolha= Coordenador('Maria', 50,'111.111.111-11', 'Coordenador')
        elif (opcao==3):
            self.escolha= Servidor('Marcos', 40,'111.222.333-44', 'Servidor')
        elif (opcao==4):
            print('Você está saindo')
        else:
            self.menu()
    def __str__(self):
        return f'{self.escolha}'


menu= Main()
print(menu)
print('')
cont=0
while(cont==0):
    print('O que deseja fazer:')
    print('1- Voltar ao menu')
    print('2- Sair')
    opcao= int(input('Qual opção?'))
    if(opcao==1):
        menu= Main()
        print(menu)
        print('')
    else:
        print('Você esta saindo')
        cont=1

