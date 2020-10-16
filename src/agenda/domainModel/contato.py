class Contato:

    def __init__(self, nome, numero):
        if nome == "" or nome is None:
            raise ValueError("Nome é obrigatório")

        if numero == "" or numero is None:
            raise ValueError("Numero é obrigatório")

        if len(nome) > 50:
            raise ValueError("Nome maior que 50 caracteres")

        if len(numero) > 15:
            raise ValueError("Número maior que 15 digitos")

        self.nome = nome
        self.numero = numero
