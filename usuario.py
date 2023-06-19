class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.livros_emprestados = []

    def obter_nome(self):
        return self.nome

    def obter_email(self):
        return self.email

    def adicionar_emprestimo(self, emprestimo):
        self.livros_emprestados.append(emprestimo.livro)

    def remover_emprestimo(self, emprestimo):
        self.livros_emprestados.remove(emprestimo.livro)
