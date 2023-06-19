from emprestimo import Emprestimo
from devolucao import Devolucao

class Biblioteca:
    def __init__(self, livro_service, usuario_service):
        self.livro_service = livro_service
        self.usuario_service = usuario_service

    def adicionar_livro(self, livro):
        return self.livro_service.adicionar_livro(livro)

    def remover_livro(self, livro):
        return self.livro_service.remover_livro(livro)

    def buscar_livro(self, titulo):
        return self.livro_service.buscar_livro(titulo)

    def adicionar_usuario(self, usuario):
        return self.usuario_service.adicionar_usuario(usuario)

    def remover_usuario(self, usuario):
        return self.usuario_service.remover_usuario(usuario)

    def buscar_usuario(self, nome):
        return self.usuario_service.buscar_usuario(nome)

    def emprestar_livro(self, livro, usuario):
        emprestimo = Emprestimo(livro, usuario)
        return emprestimo.emprestar_livro()

    def devolver_livro(self, emprestimo):
        devolucao = Devolucao(emprestimo)
        resultado = devolucao.devolver()
        return resultado