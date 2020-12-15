from persistencia.abstract_dao import AbstractDAO
from entidade.usuario import Usuario


class UsuarioDAO(AbstractDAO):
    def __init__(self):
        super().__init__('usuarios.pkl')

    def add(self, usuario: Usuario):
        if ((usuario is not None) and (isinstance(usuario, Usuario))
             and (isinstance(usuario.nome_usuario, str))):
             super().add(usuario.nome_usuario, usuario)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, str):
            super().remove(key)
