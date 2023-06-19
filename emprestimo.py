class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario

    def emprestar_livro(self):
        if(self != None):
            if self.livro.esta_disponivel():
                self.usuario.adicionar_emprestimo(self)
                self.livro.definir_disponibilidade(False)
                return [self, f"Livro '{self.livro.obter_titulo()}' emprestado para {self.usuario.obter_nome()}."]
            else:
                return [None, f"Livro '{self.livro.obter_titulo()}' não está disponível para empréstimo."]
