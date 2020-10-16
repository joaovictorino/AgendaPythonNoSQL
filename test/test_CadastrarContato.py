import pytest
from test.mock.memoryRepositoryContato import MemoryRepositoryContato
from agenda.domainModel.service.cadastrarContato import CadastrarContato
from agenda.domainModel.contato import Contato
from agenda.domainModel.exception.contatoJaCadastrado import ContatoJaCadastrado

def test_CadastrarContatoSucesso():
    repository = MemoryRepositoryContato()
    service = CadastrarContato()
    contato = Contato("Pedro", "(11) 975854589")
    service.executar(contato, repository)

def test_CadastrarContatoJaCadastrado():
    repository = MemoryRepositoryContato()
    service = CadastrarContato()
    contato = Contato("Pedro", "(11) 975854589")
    service.executar(contato, repository)

    with pytest.raises(ContatoJaCadastrado):
        service.executar(contato, repository)
