from limite.tela_projeto import TelaProjeto
from entidade.projeto import Projeto
from limite.tela_add_projeto import TelaAddProjeto
from persistencia.projeto_dao import ProjetoDAO
from limite.tela_edit_projeto import TelaEditProjeto


class ControladorProjeto:
    def __init__(self, controlador_principal):
        self.__controlador = controlador_principal
        self.__tela_projeto = TelaProjeto(self)
        self.__tela_add_projeto = TelaAddProjeto()
        self.__projeto_dao = ProjetoDAO()
        self.__tela_edit_projeto = TelaEditProjeto()
        self.__exibindo_tela = True

    def adicionar_projeto(self):
        botao, dados_projeto = self.__tela_add_projeto.open()
        print(dados_projeto)
        novo_projeto = Projeto(dados_projeto["titulo"], 
                               int(dados_projeto["codigo"]), 
                               dados_projeto["descricao"], 
                               dados_projeto["custo"])
                               
        self.__projeto_dao.add(novo_projeto)
        self.__tela_add_projeto.show_message('Cadastro de Projeto', 'Projeto criado com sucesso')

    def remover_projeto(self, projeto: Projeto):
        if isinstance(projeto, Projeto):
            self.__projeto_dao.remove(projeto.codigo)

    def projetos(self):
        return self.__projeto_dao.get_all()

    def editar_projeto(self, edition):
        botao, editarce = self.__tela_edit_projeto.open()

    def voltar(self):
        self.__exibindo_tela = False

    def abre_tela(self):
        self.__exibindo_tela = True
        lista_opcoes = {'bt_1': self.adicionar_projeto,
						'bt_2': self.remover_projeto,
                        'bt_3': self.editar_projeto,
				        'bt_0': self.voltar}
        while self.__exibindo_tela:
            opcao_escolhida, values = self.__tela_projeto.open(self.__projeto_dao.get_all())
            if opcao_escolhida is None:
                opcao_escolhida = 'bt_0'
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if opcao_escolhida == 'bt_0' or opcao_escolhida == 'bt_1':
                funcao_escolhida()
            else:
                try:
                    funcao_escolhida(values['list_1'][0])
                except IndexError:
                    self.__tela_projeto.show_message('Erro', 'Nada foi selecionado')
                
