from agenda.domainModel.abstract.abstractRepositoryContato import AbstractRepositoryContato
from agenda.domainModel.contato import Contato
from agenda.domainModel.service.cadastrarContato import CadastrarContato

class AgendaService:

    def __init__(self, repository: AbstractRepositoryContato):
        self.repository = repository

    def buscar(self, nome):
        contatos = self.repository.buscar(nome)
        listDTO = []
        for contato in contatos:
            listDTO.append({ "nome" : contato.nome, "numero" : contato.numero })
        return listDTO

    def inserir(self, nome, numero):
        contato = Contato(nome, numero)
        service = CadastrarContato().executar(contato, self.repository)
        