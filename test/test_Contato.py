import pytest
from agenda.domainModel.contato import Contato

def test_NomeMaiorQue50Caracteres():
    nome = "Joao Henrique Victorino da Silva Ferreira Andrade Domingues"
    numero = "(11) 97505-6542"
    with pytest.raises(ValueError):
        contato = Contato(nome, numero)

def test_NomeBranco():
    numero = "(11) 97505-6542"
    with pytest.raises(ValueError):
        contato = Contato("", numero)

def test_NomeNone():
    numero = "(11) 97505-6542"
    with pytest.raises(ValueError):
        contato = Contato(None, numero)

def test_NumeroMaiorQue25Digitos():
    nome = "José da Silva"
    numero = "+ 55 (11) 97303-6518"
    with pytest.raises(ValueError):
        contato = Contato(nome, numero)

def test_NovoContatoSucesso():
    nome = "José da Silva"
    numero = "(11) 97505-6542"
    contato = Contato(nome, numero)

def test_NumeroBranco():
    nome = "Joao Henrique Victorino"
    with pytest.raises(ValueError):
        contato = Contato(nome, "")

def test_NumeroNone():
    nome = "Joao Henrique Victorino"
    with pytest.raises(ValueError):
        contato = Contato(nome, None)
