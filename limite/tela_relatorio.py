from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaRelatorio(TelaAbstrata):
    def __init__(self, controlador_relatorio):
        super().__init__(controlador_relatorio)
        self.__window = None
        self.init_components()

    def init_components(self):
        coluna_1 = [[sg.Button(button_text='Gerar Relatório de Projetos', key='bt_1', enable_events=True, size=(40, 1))],
                    [sg.Button(button_text='Gerar Relatório de Tarefas', key='bt_2', enable_events=True, size=(40, 1))],   
                    [sg.Button(button_text='Voltar', key='bt_0', enable_events=True, size=(40, 1))]]
        layout = [[sg.Text('Adquirir Relatório', size=(15, 1), font=("Helvetica", 25))],
                  [sg.Column(coluna_1)]]
        
        self.__window = sg.Window('Adquirir Relatório', default_element_size= (40, 1),
                                  element_justification='center').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        self.close()
        return button, values

    def close(self):
        self.__window.Close()
    
    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
