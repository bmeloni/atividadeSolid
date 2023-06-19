class LivroService:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        if livro.esta_disponivel():
            self.livros.append(livro)
            return f"Livro '{livro.obter_titulo()}' adicionado à biblioteca."
        else:
            return f"Livro '{livro.obter_titulo()}' não está disponível."

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            return f"Livro '{livro.obter_titulo()}' removido da biblioteca."
        else:
            return f"Livro '{livro.obter_titulo()}' não está na biblioteca."

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.obter_titulo() == titulo:
                return livro
        return None
