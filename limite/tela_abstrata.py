from abc import ABC, abstractmethod


class TelaAbstrata(ABC):
  @abstractmethod
  def __init__(self, controlador):
    self.__controlador = controlador

  def le_num_inteiro(self, valor_lido: str = "", inteiros_validos: [] = None):
	  while True:
		  #valor_lido = input(mensagem)
		  try:
			  inteiro = int(valor_lido)
			  if inteiros_validos and inteiro not in inteiros_validos:
				  raise ValueError
			  return inteiro
		  except ValueError:
			  print("Valor escolhido incorreto, Digite um valor válido")
			  if inteiros_validos:
				  #popup
				  print("Valores Válidos: ", inteiros_validos)

  @property
  def controlador(self):
    return self.__controlador