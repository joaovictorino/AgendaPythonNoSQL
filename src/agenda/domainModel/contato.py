class Contato:

    def __init__(self, nome, numero):
        if len(nome) > 200:
            raise ValueError("Nome maior que 200 caracteres")

        if len(numero) > 25:
            raise ValueError("Número maior que 25 digitos")

        self.nome = nome
        self.numero = numero
