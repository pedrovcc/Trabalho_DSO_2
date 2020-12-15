from persistencia.abstract_dao import AbstractDAO
from entidade.tarefa import Tarefa


class TarefaDAO(AbstractDAO):
    def __init__(self):
        super().__init__('tarefa.pkl')

    def add(self, tarefa: Tarefa):
        if ((tarefa is not None) and (isinstance(tarefa, Tarefa))
             and (isinstance(tarefa.titulo_tarefa, str))):
             super().add(tarefa.titulo_tarefa, tarefa)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, str):
            super().remove(key)
