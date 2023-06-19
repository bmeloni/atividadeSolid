class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def obter_titulo(self):
        return self.titulo

    def obter_autor(self):
        return self.autor

    def obter_ano_publicacao(self):
        return self.ano_publicacao

    def esta_disponivel(self):
        return self.disponivel

    def definir_disponibilidade(self, status):
        self.disponivel = status
