from limite.tela_usuario import TelaUsuario
from entidade.usuario import Usuario
from limite.tela_usuario_2 import TelaUsuario_2
from persistencia.usuario_dao import UsuarioDAO
from limite.tela_setor_remover import TelaConfirmacao


class ControladorUsuario:
  def __init__(self, controlador_principal):
    self.__controlador = controlador_principal
    self.__tela_usuario = TelaUsuario(self)
    self.__tela_usuario_2 = TelaUsuario_2()
    self.__exibindo_tela = True
    self.__usuario_dao = UsuarioDAO()
    self.__tela_setor_remover = TelaConfirmacao()

  def adicionar_usuario(self):
    botao, dados_usuario = self.__tela_usuario_2.open()
    novo_usuario = Usuario(dados_usuario["nome_usuario"], dados_usuario["id_usuario"])
    if botao == 'bt_1':
      self.__usuario_dao.add(novo_usuario)
      self.__tela_usuario_2.show_message('Cadastro de Usuário', 'Usuário adicionado com sucesso!')

  def remover_usuario(self, usuario: Usuario):
    if isinstance(usuario, Usuario):
      self.__usuario_dao.remove(usuario.nome_usuario)

  def voltar(self):
    self.__exibindo_tela = False

  def abre_tela(self):
    self.__exibindo_tela = True
    lista_opcoes = {'bt_1': self.adicionar_usuario,
						        'bt_2': self.remover_usuario, 
						        'bt_0': self.voltar}
    while self.__exibindo_tela:
      opcao_escolhida, values = self.__tela_usuario.open(self.__usuario_dao.get_all())
      if opcao_escolhida is None:
        opcao_escolhida = 'bt_0'
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      if opcao_escolhida == 'bt_0' or opcao_escolhida == 'bt_1':
        funcao_escolhida()
      else:
        try:
          funcao_escolhida(values['list_1'][0])
        except IndexError:
          self.__tela_usuario.show_message('Erro', 'Nada foi selecionado')
