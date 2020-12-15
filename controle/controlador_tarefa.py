from limite.tela_tarefa import TelaTarefa
from entidade.tarefa import Tarefa
from controle.controlador_projeto import ControladorProjeto
from persistencia.tarefa_dao import TarefaDAO
from limite.tela_add_tarefa import TelaAddTarefa
from limite.tela_edit_projeto import TelaEditProjeto


class ControladorTarefa:
    def __init__(self, controlador_principal):
        self.__controlador = controlador_principal
        self.__tela_tarefa = TelaTarefa(self)
        self.__exibindo_tela = True
        self.__tarefa_dao = TarefaDAO()
        self.__tela_edit_tarefa = TelaEditProjeto()
        self.__tela_add_tarefa = TelaAddTarefa()
        

    def adicionar_tarefa(self):
        botao, dados_tarefa = self.__tela_add_tarefa.open()
        nova_tarefa = Tarefa(dados_tarefa["titulo_tarefa"], 
                             dados_tarefa["descricao_tarefa"], 
                             dados_tarefa["prazo_tarefa"], 
                             dados_tarefa["situacao_tarefa"])
        self.__tarefa_dao.add(nova_tarefa)
        self.__tela_add_tarefa.show_message('Cadastro de Tarefa', 'Tarefa criada com Sucesso!')
    
    def tarefas(self):
        return self.__tarefa_dao.get_all()

    def remover_tarefa(self, tarefa: Tarefa):
        if isinstance(tarefa, Tarefa):
            self.__tarefa_dao.remove(tarefa.titulo_tarefa)
    
    def editar_tarefa(self, edition):
        botao, editarce = self.__tela_edit_tarefa.open()

    def voltar(self):
        self.__exibindo_tela = False

    def abre_tela(self):
        self.__exibindo_tela = True
        lista_opcoes = {'bt_1': self.adicionar_tarefa,
                        'bt_2': self.remover_tarefa,
                        'bt_3': self.editar_tarefa, 
                        'bt_0': self.voltar}
        while self.__exibindo_tela:
            opcao_escolhida, values = self.__tela_tarefa.open(self.__tarefa_dao.get_all())
            if opcao_escolhida is None:
                opcao_escolhida = 'bt_0'
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if opcao_escolhida == 'bt_0' or opcao_escolhida == 'bt_1':
                funcao_escolhida()
            else:
                try:
                    funcao_escolhida(values['list_1'][0])
                except IndexError:
                    self.__tela_tarefa.show_message('Erro', 'Nada foi selecionado')
