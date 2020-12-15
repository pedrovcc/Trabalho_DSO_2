from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaPrincipal(TelaAbstrata):
  def __init__(self, controlador_principal):
    super().__init__(controlador_principal)
    self.__window = None
    self.init_components()

  def init_components(self):
    sg.theme('DarkTeal6')
    coluna_1 = [[sg.Text('Escolha uma opção:', justification='center', size=(40, 1))],
                [sg.Button(button_text='Cadastrar Projeto', key='bt_1', enable_events=True, size =(40, 1))],
                [sg.Button(button_text='Cadastrar Tarefa', key='bt_2', enable_events=True, size =(40, 1))],
                [sg.Button(button_text='Cadastrar Usuario', key='bt_3', enable_events=True, size =(40, 1))],
                [sg.Button(button_text='Cadastrar Setor', key='bt_4', enable_events=True, size =(40, 1))],
                [sg.Button(button_text='Visualizar Relatorios', key='bt_5', enable_events=True, size =(40, 1))],
                [sg.Button(button_text='Encerrar Sistema', key='bt_6', enable_events=True, size =(40, 1))]]
    layout = [[sg.Text('Gerenciador de Projetos', size = (20, 1),font = ("Helvetica", 20), justification='center')],
              [sg.Column(coluna_1)]]

    self.__window = sg.Window('Gerenciador de Projetos', default_element_size=(40, 1), 
                              element_justification='center').Layout(layout)

  def open(self):
    button, values = self.__window.Read()
    self.close()
    return button, values

  def close(self):
    self.__window.Close()

  def show_message(self, titulo: str, mensagem: str):
    sg.Popup('Oi', 'Ola')