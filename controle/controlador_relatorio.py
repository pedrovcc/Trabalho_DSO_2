from limite.tela_relatorio import TelaRelatorio
from datetime import datetime


class ControladorRelatorio:
    def __init__(self, controlador_principal):
        self.__controlador = controlador_principal
        self.__tela_relatorio = TelaRelatorio(self)
        self.__exibindo_tela = True
        

    def gerar_relatorio_projeto(self):
        projetos = self.__controlador.controlador_projeto.projetos()
        logFilePathParser = "C:/Users/pedro/OneDrive/Área de Trabalho/Trabalho_dso_2/Gerenciador_Projeto/logs/Logs_Projetos.txt"
        logParser = open(logFilePathParser,'w')
        logParserArray = []
        logParserArray.append("----------ARQUIVO DE LOG GERENCIADOR DE PROJETOS----------\n")
        logParserArray.append('DATA DA CRIACAO: '+str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        logParserArray.append("\nPROJETOS EXISTENTES:\n")
        for projeto in projetos:
            logParserArray.append('Código: {0} - Título: {1} - Descrição: {2} -  Custo: R${3}'.format(projeto.codigo, projeto.titulo, 
                                                                                                      projeto.descricao, projeto.custo)) 
            logParserArray.append("\n")
        logParser.writelines(logParserArray)
        logParser.close()
        aviso = self.__tela_relatorio.show_message('Atenção', 'O relatório foi gerado!')

    def gerar_relatorio_tarefa(self):
        tarefas = self.__controlador.controlador_tarefa.tarefas()
        logFilePathParser = "C:/Users/pedro/OneDrive/Área de Trabalho/Trabalho_dso_2/Gerenciador_Projeto/logs/Logs_Tarefas.txt"
        logParser = open(logFilePathParser,'w')
        logParserArray = []
        logParserArray.append("----------ARQUIVO DE LOG GERENCIADOR DE PROJETOS----------\n")
        logParserArray.append('DATA DA CRIACAO: '+str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        logParserArray.append("\nTAREFAS EXISTENTES:\n")
        for tarefa in tarefas:
            logParserArray.append('Título: {0} - Descrição: {1} - Prazo de Entrega: {2} -  Situação: R${3}'.format(tarefa.titulo_tarefa, tarefa.descricao_tarefa, 
                                                                                                                    tarefa.prazo_tarefa, tarefa.situacao_tarefa)) 
            logParserArray.append("\n")
        logParser.writelines(logParserArray)
        logParser.close()
        aviso = self.__tela_relatorio.show_message('Atenção', 'O relatório foi gerado!')

    def voltar(self):
        self.__exibindo_tela = False

    def abre_tela(self):
        self.__exibindo_tela = True
        lista_opcoes = {'bt_1':self.gerar_relatorio_projeto,
                        'bt_2':self.gerar_relatorio_tarefa,
                        'bt_0': self.voltar}

        while self.__exibindo_tela:
            opcao_escolhida, values = self.__tela_relatorio.open()
            if opcao_escolhida is None:
                opcao_escolhida = 'bt_0'
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
