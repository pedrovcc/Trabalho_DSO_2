

class Tarefa:
    def __init__(self, titulo_tarefa: str, descricao_tarefa: str, prazo_tarefa: str, situacao_tarefa: str):
        if isinstance(titulo_tarefa, str):
            self.__titulo_tarefa = titulo_tarefa
        if isinstance(descricao_tarefa, str):
            self.__descricao_tarefa = descricao_tarefa
        if isinstance(prazo_tarefa,str):
            self.__prazo_tarefa = prazo_tarefa
        if isinstance(situacao_tarefa, str):
            self.__situacao_tarefa = situacao_tarefa

    def __str__(self):
        return '{0} - {1}'.format(self.__titulo_tarefa, self.__situacao_tarefa)

    @property
    def titulo_tarefa(self):
        return self.__titulo_tarefa

    @titulo_tarefa.setter
    def titulo_tarefa(self, titulo_tarefa: str):
        if isinstance(titulo_tarefa, str):
            self.__titulo_tarefa = titulo_tarefa

    @property
    def descricao_tarefa(self):
        return self.__descricao_tarefa

    @descricao_tarefa.setter
    def descricao_tarefa(self, descricao_tarefa: str):
        if isinstance(descricao_tarefa, str):
            self.__descricao_tarefa = descricao_tarefa

    @property
    def prazo_tarefa(self):
        return self.__prazo_tarefa

    @prazo_tarefa.setter
    def prazo_tarefa(self, prazo_tarefa: str):
        if isinstance(prazo_tarefa, str):
            self.__prazo_tarefa = prazo_tarefa

    @property
    def situacao_tarefa(self):
        return self.__situacao_tarefa

    @situacao_tarefa.setter
    def situacao_tarefa(self, situacao_tarefa: str):
        if isinstance(situacao_tarefa, str):
            self.__situacao_tarefa = situacao_tarefa
