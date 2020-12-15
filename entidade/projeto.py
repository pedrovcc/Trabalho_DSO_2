from entidade.tarefa import Tarefa
from entidade.usuario import Usuario


class Projeto:
    def __init__(self, titulo: str, codigo: int, descricao: str, custo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(custo, str):
            self.__custo = custo
        '''if isinstance(tarefa, Tarefa):
            self.tarefas = []'''
    
    def __str__(self):
        return '{0:03} - {1}'.format(self.__codigo, self.__titulo)

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter  
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, custo: str):
        if isinstance(custo, str):
            self.__custo = custo

    #criar property de tarefas
    # e um metodo adiciona tarefas
