from emprestimo import Emprestimo

class Devolucao:
    def __init__(self, emprestimo):
        self.emprestimo = emprestimo

    def devolver(self):
        if(self != None):
            self.emprestimo.usuario.remover_emprestimo(self.emprestimo)
            self.emprestimo.livro.definir_disponibilidade(True)
            return f"Livro '{self.emprestimo.livro.obter_titulo()}' devolvido por {self.emprestimo.usuario.obter_nome()}."
