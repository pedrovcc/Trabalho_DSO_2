import PySimpleGUI as sg


class TelaSetor_2:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('Adicionar Setor', size = (20, 1), font=("Helvetica", 25))],
                  [sg.Text('Nome', size=(15, 1)), sg.InputText('', key='nome_setor')],
                  [sg.Text('')],
                  [sg.Button(button_text='Salvar', key='bt_1', enable_events=True),
                   sg.Cancel(button_text='Cancelar', key='bt_2')]]
        self.__window = sg.Window('Adicionar Setor', default_element_size=(20, 1)).Layout(layout)

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        self.close()
        return button, values

    def close(self):
        self.__window.Close()
