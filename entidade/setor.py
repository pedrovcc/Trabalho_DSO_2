

class Setor:
  def __init__(self, nome_setor: str):
    if isinstance(nome_setor, str):
      self.__nome_setor = nome_setor

  def __str__(self):
    return '{0}'.format(self.nome_setor)

  @property
  def nome_setor(self):
    return self.__nome_setor

  @nome_setor.setter
  def nome_setor(self, nome_setor: str):
    if isinstance(nome_setor, str):
      self.__nome_setor
