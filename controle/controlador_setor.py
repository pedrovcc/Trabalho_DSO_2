from limite.tela_setor import TelaSetor
from limite.tela_setor_2 import TelaSetor_2
from limite.tela_setor_remover import TelaConfirmacao
from entidade.setor import Setor
from controle.controlador_usuario import ControladorUsuario
from persistencia.setor_dao import SetorDAO


class ControladorSetor:
  def __init__(self, controlador_principal):
    self.__setor_dao = SetorDAO()
    self.__controlador = controlador_principal
    self.__tela_setor = TelaSetor(self)
    self.__tela_setor_2 = TelaSetor_2()
    self.__tela_setor_remover = TelaConfirmacao()
    self.__exibindo_tela = True

  def adicionar_setor(self):
    botao, dados_setor = self.__tela_setor_2.open()
    novo_setor = Setor(dados_setor["nome_setor"])
    if botao == 'bt_1':
      self.__setor_dao.add(novo_setor)
      self.__tela_setor.show_message('Cadastro de Setor', 'Setor adicionado com sucesso!')

  def remover_setor(self, setor: Setor):
    if isinstance(setor, Setor):
            self.__setor_dao.remove(setor.nome_setor)

  def voltar(self):
    self.__exibindo_tela = False

  def abre_tela(self):
    self.__exibindo_tela = True
    lista_opcoes = {'bt_1': self.adicionar_setor,
						        'bt_2': self.remover_setor, 
						        'bt_0': self.voltar,}
    while self.__exibindo_tela:
      opcao_escolhida, setor = self.__tela_setor.open(self.__setor_dao.get_all())
      if opcao_escolhida is None:
        opcao_escolhida = 'bt_0'
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      if opcao_escolhida == 'bt_0' or opcao_escolhida == 'bt_1':
        funcao_escolhida()
      else:
        funcao_escolhida(setor['list_1'][0])
