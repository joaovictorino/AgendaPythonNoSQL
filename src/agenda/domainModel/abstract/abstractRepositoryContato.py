import abc
from agenda.domainModel.contato import Contato

class AbstractRepositoryContato:

    @abc.abstractmethod
    def buscar(self, nome) -> [Contato]:
        pass

    @abc.abstractmethod
    def inserir(self, contato):
        pass