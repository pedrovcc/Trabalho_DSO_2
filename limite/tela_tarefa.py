from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaTarefa(TelaAbstrata):
    def __init__(self, controlador_tarefa):
        super().__init__(controlador_tarefa)
        self.__window = None
        self.init_components()

    def init_components(self, tarefas = []):
        coluna_1 = [[sg.Button(button_text='Adicionar Tarefa', key='bt_1', enable_events=True, size=(40, 1))],
                    [sg.Button(button_text='Remover Tarefa', key='bt_2', enable_events=True, size=(40, 1))],
                    [sg.Button(button_text='Editar Tarefa', key='bt_3', enable_events=True, size=(40, 1))],
                    [sg.Button(button_text='Voltar', key='bt_0', enable_events=True, size=(40, 1))]]
        layout = [[sg.Text('Cadastrar Tarefa', size = (15,1), font=("Helvetica", 25))],
                  [sg.Column(coluna_1)],
                  [sg.Listbox(values=(list(tarefas)), size=(44, 8), select_mode='single', key='list_1')]]
                
        self.__window = sg.Window('Cadastrar Tarefa', default_element_size = (40, 1),
                                  element_justification='center').Layout(layout)   

    def open(self, tarefas):
        self.init_components(tarefas)
        button, values = self.__window.Read()
        self.close()
        return button, values

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)