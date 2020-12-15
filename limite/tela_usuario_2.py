  
#from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaUsuario_2:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('Adicionar Usuário', justification='center' ,size = (20, 1),font=("Helvetica", 25))],
                  [sg.Text('Nome', size=(7, 1), justification='right'), sg.InputText('', key='nome_usuario')],
                  [sg.Text('Id', size=(7, 1), justification='right'), sg.InputText('', key='id_usuario')],
                  [sg.Text('')],
                  [sg.Button(button_text='Salvar', key='bt_1', enable_events=True),
                   sg.Cancel(button_text='Cancelar', key='bt_2')]]

        self.__window = sg.Window('Adicionar Usuário', default_element_size=(20, 1),
                                  element_justification='center').Layout(layout)

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        self.close()
        return button, values

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
