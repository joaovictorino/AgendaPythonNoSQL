import pytest
from agenda.domainModel.contato import Contato

def test_NomeMaiorQue200Caracteres():
    nome = "fjdlfkjhfkjfdhkjfhsdfljksdhfjkdshfjkdfsdkfhslkjhfakdjfhsdkjfhsdkjfhdsfkljsdhfksldjfhsdkfjdshkfjhsdkfjhdsfkljhsdklhfsrtetretretretretrterfddgert5rtergfdgdfgfdgtrtretrtretfdgfdgfgdfgfdtretreewrdfdsesserresrer"
    numero = "(11) 97505-6542"
    with pytest.raises(ValueError):
        contato = Contato(nome, numero)

def test_NumeroMaiorQue25Digitos():
    nome = "José da Silva"
    numero = "(11) 97505-654245454545558"
    with pytest.raises(ValueError):
        contato = Contato(nome, numero)

def test_NovoContatoSucesso():
    nome = "José da Silva"
    numero = "(11) 97505-65424"
    contato = Contato(nome, numero)
