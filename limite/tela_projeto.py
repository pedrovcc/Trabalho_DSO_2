from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaProjeto(TelaAbstrata):
    def __init__(self, controlador_projeto):
        super().__init__(controlador_projeto)
        self.__window = None
        self.init_components()

    def init_components(self, projetos = []):
        coluna_1 = [[sg.Button(button_text='Adicionar Projeto', key='bt_1', enable_events=True, size=(40, 1))],
                    [sg.Button(button_text='Remover Projeto', key='bt_2', enable_events=True, size=(40, 1))],
                    [sg.Button(button_text='Editar Projeto', key='bt_3', enable_events=True, size=(40, 1))],
                    [sg.Button(button_text='Voltar', key='bt_0', enable_events=True, size=(40, 1))]]
        layout = [[sg.Text('Cadastrar Projeto', size = (15,1), font=("Helvetica", 25))],
                  [sg.Column(coluna_1)],
                  [sg.Listbox(values=(list(projetos)), size=(44, 8), select_mode='single', key='list_1')]]
                
        self.__window = sg.Window('Cadastrar Projeto', default_element_size = (40, 1),
                                  element_justification='center').Layout(layout)   

    def open(self, projetos):
        self.init_components(projetos)
        button, values = self.__window.Read()
        self.close()
        return button, values
    
    def valores(self, projetos):
        values = self.__window.Read()
        return values
    

    
    def close(self):
        self.__window.Close()
    
    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)