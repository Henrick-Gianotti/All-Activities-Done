import sys
import os
import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from main_window import Ui_MainWindow
from tela_cadastro import Ui_tela_cadastro
from tela_consulta import Ui_tela_consulta

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao_cadastrar.clicked.connect(self.abrir_tela_cadastro)
        self.ui.botao_consultar.clicked.connect(self.abrir_tela_consulta)

    def abrir_tela_cadastro(self):
        self.tela_cadastro = TelaCadastro(self) 
        self.tela_cadastro.show()
        self.hide()
    
    def abrir_tela_consulta(self):
        self.tela_consulta = TelaConsulta(self)  
        self.tela_consulta.show()
        self.hide()

class TelaCadastro(QMainWindow):
    def __init__(self, main_window):
        super(TelaCadastro, self).__init__()
        self.ui = Ui_tela_cadastro()
        self.ui.setupUi(self)
        self.main_window = main_window

        self.ui.botao_salvar.clicked.connect(self.salvar_cadastro)
        
    def salvar_cadastro(self):
        data = {
            "nome": self.ui.input_nome.text(),
            "idade": self.ui.input_idade.value(),
            "peso": self.ui.input_peso.value(),
            "altura": self.ui.input_altura.value(),
            "sexo": "Feminino" if self.ui.botao_feminino.isChecked() else "Masculino" if self.ui.botao_masculino.isChecked() else "Não informado",
            "objetivo": "Emagrecer" if self.ui.botao_emagrecer.isChecked() else "Engordar" if self.ui.botao_engordar.isChecked() else "Ficar saudável" if self.ui.botao_dieta.isChecked() else "Nada informado"
        }

        # salvar na pasta users
        users_folder = os.path.join(os.getcwd(), 'users')
        os.makedirs(users_folder, exist_ok=True)

        nome_arquivo = self.ui.input_nome.text().strip()
        if not nome_arquivo:
            QMessageBox.warning(self, "Erro", "O nome não pode estar vazio!")
            return

        # caminho da pasta users
        file_path = os.path.join(users_folder, f"{nome_arquivo}.json")

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            QMessageBox.information(self, "Sucesso", "Cadastro salvo com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar: {e}")

        self.close() 
        self.main_window.show()

class TelaConsulta(QMainWindow):
    def __init__(self, main_window):
        super(TelaConsulta, self).__init__()
        self.ui = Ui_tela_consulta()
        self.ui.setupUi(self)
        self.main_window = main_window

        self.ui.botao_consultar_user.clicked.connect(self.consultar_user)
        self.ui.botao_menu.clicked.connect(self.voltar)
        self.ui.botao_voltar.clicked.connect(self.reconsultar)
        self.ui.consulta_obj.hide()
        self.ui.consulta_lista.hide()
        self.ui.botao_menu.hide()

    def consultar_user(self):
        self.ui.botao_menu.hide()
        self.ui.consulta_obj.show()
        self.ui.label_info.hide()

        nome_usuario = self.ui.input_user.text().strip()
        # verifica se o campo não está vazio
        if not nome_usuario:
            QMessageBox.warning(self, "Erro", "O nome não pode estar vazio!")
            return

        # codigo para indicar a pasta que será salva (praticamente um BD)
        users_folder = os.path.join(os.getcwd(), 'users')
        # codigo para indicar o caminho da pasta
        file_path = os.path.join(users_folder, f"{nome_usuario}.json")

        # verifica se o usuário realmente exite
        if not os.path.exists(file_path):
            QMessageBox.warning(self, "Erro", "Usuário não encontrado!")
            return

        # pega as infos do json
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                dados = json.load(file)

            self.ui.consulta_obj.setText(f"Objetivo: {dados['objetivo']}")
            self.ui.consulta_lista.setText(f"Idade: {dados['idade']}\nPeso: {dados['peso']}\nAltura: {dados['altura']}\nSexo: {dados['sexo']}\nObjetivo: {dados['objetivo']}")

            # verifica o objetivo e já mostra a lista
            if dados['objetivo'] == "Engordar":
                self.ui.consulta_lista.setText(self.ui.consulta_lista.text() + "\n\n(De manhã) Comer 5 pães com nutella\n(Almoço) Comer salgado (de preferência coxinha)\n(De tarde) Comer aquele pastelão de 10 contos\n(Janta) Comer aquela feijoada")
            elif dados['objetivo'] == "Emagrecer":
                self.ui.consulta_lista.setText(self.ui.consulta_lista.text() + "\n\n(De manhã) Come nada, emagrece mais rápido ainda\n(Almoço) Toma apenas um suco natural\n(Tarde) Agora você pode comer um pão com manteiga\n(Janta) Salada apenas, para fortalecer as fibras e vitaminas")
            else:
                self.ui.consulta_lista.setText(self.ui.consulta_lista.text() + "\n\n(De manhã) 1 bananinha e uma goiaba\n(Almoço) Arroz e feijão, salada e macarrão\n(Tarde) Pão e aquele cafézinho\n(Janta) Arroz e carne acebolado")

            self.ui.consulta_obj.show()
            self.ui.consulta_lista.show()

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro: {e}")

    def voltar(self):
        self.close()
        self.main_window.show()

    def reconsultar(self): # praticamente uma função pra esconder e mostrar os botoes
        self.ui.consulta_obj.hide()
        self.ui.consulta_lista.hide()
        self.ui.label_info.show()
        self.ui.botao_menu.show()
        self.ui.input_user.show()
        self.ui.botao_consultar_user.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec_())