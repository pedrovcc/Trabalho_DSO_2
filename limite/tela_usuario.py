from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaUsuario(TelaAbstrata):
  def __init__(self, controlador_usuario):
    super().__init__(controlador_usuario)
    self.__window = None
    self.init_components()

  def init_components(self, usuarios = []):
    coluna_1 = [[sg.Button(button_text='Adicionar Usuário', key='bt_1', enable_events=True, size=(40, 1))],
                [sg.Button(button_text='Remover Usuário', key='bt_2', enable_events=True, size=(40, 1))],
                [sg.Button(button_text='Voltar', key='bt_0', enable_events=True, size=(40, 1))]]
    layout = [[sg.Text('Cadastrar Usuário', size = (15,1), font=("Helvetica", 25))],
              [sg.Column(coluna_1)],
              [sg.Listbox(values=(list(usuarios)), size=(44, 3), select_mode='single', key='list_1')]]

    self.__window = sg.Window('Cadastrar Usuário', default_element_size = (40, 1),
                               element_justification='center').Layout(layout)

  def open(self, usuarios):
    self.init_components(usuarios)
    button, values = self.__window.Read()
    self.close()
    return button, values

  def close(self):
    self.__window.Close()

  def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
