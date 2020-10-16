from agenda.domainModel.abstract.abstractRepositoryContato import AbstractRepositoryContato
from agenda.domainModel.contato import Contato

class MemoryRepositoryContato(AbstractRepositoryContato):

    def __init__(self):
        self.items = {}

    def buscar(self, nome) -> [Contato]:
        result = [contato for nomeChave, contato in self.items.items() if nome in nomeChave]
        return result

    def inserir(self, contato):
        self.items[contato.nome] = contato