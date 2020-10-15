import pymongo
import re
from agenda.domainModel.abstract.abstractRepositoryContato import AbstractRepositoryContato
from agenda.domainModel.contato import Contato

class RepositoryContato(AbstractRepositoryContato):

    def __init__(self, endereco):
        client = pymongo.MongoClient(endereco)
        self.db = client.contato
        self.db.contato.create_index("nome", unique=True)

    def buscar(self, nome) -> [Contato]:
        regexp = re.compile(".*{0}.*".format(nome), re.IGNORECASE)
        self.list = []
        items = self.db.contato.find({ "nome" : regexp })
        
        for item in items:
            self.list.append(Contato(item["nome"], item["numero"]))

        return self.list

    def inserir(self, contato):
        self.db.contato.insert_one({ "nome": contato.nome, "numero": contato.numero })