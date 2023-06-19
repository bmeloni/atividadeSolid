from livro import Livro
from biblioteca import Biblioteca
from livroService import LivroService
from usuarioService import UsuarioService
from usuario import Usuario

if __name__ == "__main__":
    livro1 = Livro("Python para Iniciantes", "John Smith", 2018)
    livro2 = Livro("Python Avançado", "Jane Doe", 2020)
    livro_service = LivroService()
    usuario_service = UsuarioService()
    biblioteca = Biblioteca(livro_service, usuario_service)
    usuario1 = Usuario("Alice", "alice@example.com")
    usuario2 = Usuario("Bob", "bob@example.com")

    print(biblioteca.adicionar_livro(livro1))
    print(biblioteca.adicionar_livro(livro2))

    print(biblioteca.adicionar_usuario(usuario1))
    print(biblioteca.adicionar_usuario(usuario2))

    emprestimo1, mensagem = biblioteca.emprestar_livro(livro1, usuario1)
    print(mensagem)
    

    emprestimo2, mensagem = biblioteca.emprestar_livro(livro1, usuario2)
    print(mensagem)

    print(biblioteca.devolver_livro(emprestimo1))

    print(biblioteca.remover_livro(livro2))
    print(biblioteca.remover_usuario(usuario2))

    livro_encontrado = biblioteca.buscar_livro("Python para Iniciantes")
    usuario_encontrado = biblioteca.buscar_usuario("Alice")

    if livro_encontrado:
        print(livro_encontrado.obter_titulo())
    if usuario_encontrado:
        print(usuario_encontrado.obter_nome())
