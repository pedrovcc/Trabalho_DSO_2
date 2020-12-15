from persistencia.abstract_dao import AbstractDAO
from entidade.projeto import Projeto


class ProjetoDAO(AbstractDAO):
    def __init__(self):
        super().__init__('projeto.pkl')

    def add(self, projeto: Projeto):
        if ((projeto is not None) and (isinstance(projeto, Projeto))
             and (isinstance(projeto.codigo, int))):
             super().add(projeto.codigo, projeto)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, int):
            super().remove(key)