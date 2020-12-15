import PySimpleGUI as sg


class TelaAddProjeto:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('Adicionar Projeto!', justification='center', size = (20, 1), font=("Helvetica", 25))],
                  [sg.Text('Titulo', size=(20, 1), justification='right'), sg.InputText('', key="titulo")],
                  [sg.Text('Código', size=(20, 1), justification='right'), sg.InputText('', key="codigo")],
                  [sg.Text('Descrição', size=(20, 1), justification='right'), sg.InputText('', key="descricao")],
                  [sg.Text('Custo', size=(20, 1), justification='right'), sg.InputText('', key="custo")],
                  [sg.Button(button_text='Salvar', size=(10, 1),  key='bt_1', enable_events=True), 
                   sg.Cancel(button_text='Cancelar', size= (10,1), key='bt_2')]]
        self.__window = sg.Window('Adicionar Projeto', default_element_size=(20, 1),
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