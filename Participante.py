class Participante():

    def __init__(self, nome, nascimento, email):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email


    def __str__(self):
        return ("Nome: %s\nNascimento: %s\nEmail: %s " % (self.nome, self.nascimento, self.email))

    def menu():
        print("\n.........Menu...........")
        print("1 Listar Participantes:")
        print("2 Adicionar Participantes")
        print("3 Sair ")

