

class Usuario:
  def __init__(self, nome_usuario: str, id_usuario: str):
    if isinstance(nome_usuario, str):
      self.__nome_usuario = nome_usuario
    if isinstance(id_usuario,str):
      self.__id_usuario = id_usuario

  def __str__(self):
    return '{0}'.format(self.nome_usuario)

  @property
  def nome_usuario(self):
    return self.__nome_usuario

  @nome_usuario.setter
  def nome_usuario(self, nome_usuario: str):
    if isinstance(nome_usuario, str):
      self.__nome_usuario

  @property
  def id_usuario(self):
    return self.__id_usuario

  @id_usuario.setter
  def id_usuario(self, id_usuario):
    if isinstance(id_usuario, str):
      self.__id_usuario
