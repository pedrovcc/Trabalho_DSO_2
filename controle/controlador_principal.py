from limite.tela_principal import TelaPrincipal
from controle.controlador_usuario import ControladorUsuario
from controle.controlador_setor import ControladorSetor
from controle.controlador_projeto import ControladorProjeto
from controle.controlador_tarefa import ControladorTarefa
from controle.controlador_relatorio import ControladorRelatorio

class ControladorPrincipal:
  def __init__(self):
    self.__tela_principal = TelaPrincipal(self)
    self.__controlador_usuario = ControladorUsuario(self)
    self.__controlador_setor = ControladorSetor(self)
    self.__controlador_projeto = ControladorProjeto(self)
    self.__controlador_tarefa = ControladorTarefa(self)
    self.__controlador_relatorio = ControladorRelatorio(self)

  @property
  def controlador_usuario(self):
    return self.__controlador_usuario

  @property
  def controlador_projeto(self):
    return self.__controlador_projeto
  
  @property
  def controlador_tarefa(self):
    return self.__controlador_tarefa

  @property
  def controlador_relatorio(self):
    return self.__controlador_relatorio

  def inicializa_sistema(self):
    self.abre_tela()

  def cadastrar_projeto(self):
    self.__controlador_projeto.abre_tela()

  def cadastrar_tarefa(self):
	  self.__controlador_tarefa.abre_tela()

  def cadastrar_usuario(self):
	  self.__controlador_usuario.abre_tela()

  def cadastrar_setor(self):
    self.__controlador_setor.abre_tela()

  def visualizar_relatorio(self):
	  self.__controlador_relatorio.abre_tela()

  def encerrar_sistema(self):
	  exit(0)

  def abre_tela(self):
    lista_opcoes = {"bt_1": self.cadastrar_projeto,
						        "bt_2": self.cadastrar_tarefa,
						        "bt_3": self.cadastrar_usuario,
						        "bt_4": self.cadastrar_setor,
						        "bt_5": self.visualizar_relatorio, 
						        "bt_6": self.encerrar_sistema}
    while True:
      opcao_escolhida, _ = self.__tela_principal.open()
      if opcao_escolhida is None:
        opcao_escolhida = 'bt_6'
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      funcao_escolhida()
      self.__tela_principal.init_components()