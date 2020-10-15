from agenda.application.agendaService import AgendaService
from agenda.domainModel.exception.contatoJaCadastrado import ContatoJaCadastrado

class Agenda:

    def __init__(self, applicationService):
        self.applicationService = applicationService

    def executar(self):
        print("Agenda")
        self.mostrarMenuPrincipal()

    def mostrarMenuPrincipal(self):
        print("Menu:")
        print("(1) Consultar contato")
        print("(2) Salvar contato")
        print("(3) Sair")
        opcao = input()
        
        if opcao == "1":
            print("Consultar contato")
            nome = self.lerNome()
            contatos = self.applicationService.buscar(nome)
            self.mostrarContatos(contatos)
        elif opcao == "2":
            print("Salvar contato")
            nome = self.lerNome()
            numero = self.lerNumero()
            try:
                self.applicationService.inserir(nome, numero)
                print("Contato cadastrado com sucesso")
            except ContatoJaCadastrado:
                print("Contato já cadastrado")
        else:
            return

        self.mostrarMenuPrincipal()

    def lerNome(self):
        return input("Informar nome: ")

    def lerNumero(self):
        return input("Informar numero: ")

    def mostrarContatos(self, contatosDTO):
        if len(contatosDTO) == 0:
            print("----------------------------------------------")
            print("Nenhum contato encontrado")
            print("----------------------------------------------")

        for contato in contatosDTO:
            print("----------------------------------------------")
            print("Nome: {0}".format(contato["nome"]))
            print("Numero: {0}".format(contato["numero"]))
            print("----------------------------------------------")
