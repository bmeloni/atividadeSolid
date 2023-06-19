class UsuarioService:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        if usuario.obter_nome() != "":
            self.usuarios.append(usuario)
            return f"Usuário '{usuario.obter_nome()}' adicionado à biblioteca."
        else:
            return "Nome de usuário inválido."

    def remover_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            return f"Usuário '{usuario.obter_nome()}' removido da biblioteca."
        else:
            return f"Usuário '{usuario.obter_nome()}' não está registrado na biblioteca."

    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.obter_nome() == nome:
                return usuario
        return None
