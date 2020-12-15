from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from persistencia.setor_dao import SetorDAO


class TelaSetor(TelaAbstrata):
  def __init__(self, controlador_setor):
    super().__init__(controlador_setor)
    self.__window = None
    self.init_components()

  def init_components(self, setores = []):
    coluna_1 = [[sg.Button(button_text='Adicionar Setor', key='bt_1', enable_events=True, size=(40, 1))],
                [sg.Button(button_text='Remover Setor', key='bt_2', enable_events=True, size=(40, 1))],
                [sg.Button(button_text='Voltar', key='bt_0', enable_events=True, size=(40, 1))]]
    layout = [[sg.Text('Cadastrar Setor', size = (15,1), font=("Helvetica", 25))],
              [sg.Column(coluna_1)],
              [sg.Listbox(values=(list(setores)), size=(44, 3), select_mode='single', key='list_1')]]
    self.__window = sg.Window('Cadastrar Setor', default_element_size = (40, 1),
                              element_justification='center').Layout(layout)

  def open(self, setores):
    self.init_components(setores)
    button, values = self.__window.Read()
    self.close()
    return button, values

  def close(self):
    self.__window.Close()

  def show_message(self, titulo: str, mensagem: str):
    sg.Popup(titulo, mensagem)
