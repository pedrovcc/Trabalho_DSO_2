from persistencia.abstract_dao import AbstractDAO
from entidade.setor import Setor


class SetorDAO(AbstractDAO):
    def __init__(self):
        super().__init__('setor.pkl')

    def add(self, setor: Setor):
        if ((setor is not None) and (isinstance(setor, Setor))
             and (isinstance(setor.nome_setor, str))):
             super().add(setor.nome_setor, setor)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, str):
            super().remove(key)
