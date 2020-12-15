import PySimpleGUI as sg


class TelaConfirmacao:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('Deseja Excluir', size = (20, 1), font=("Helvetica", 25))],
                  [sg.Text('')],
                  [sg.Button(button_text='Sim', key='sim', enable_events=True),
                   sg.Button(button_text='Não', key='nao', enable_events=True)]]
        self.__window = sg.Window('Excluir Setor', default_element_size=(20, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        self.close()
        return button, values

    def close(self):
        self.__window.Close()
  