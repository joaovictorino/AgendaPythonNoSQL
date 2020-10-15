from agenda.domainModel.abstract.abstractRepositoryContato import AbstractRepositoryContato
from agenda.domainModel.contato import Contato
from agenda.domainModel.exception.contatoJaCadastrado import ContatoJaCadastrado

class CadastrarContato:

    def executar(self, contato: Contato, repository: AbstractRepositoryContato):
        try:
            contatos = repository.buscar(contato.nome)

            if len(contatos) > 0:
                raise ContatoJaCadastrado

            repository.inserir(contato)
        except:
            raise ContatoJaCadastrado