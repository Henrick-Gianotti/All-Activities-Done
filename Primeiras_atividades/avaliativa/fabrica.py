import os

class fabrica_armas():

    def __init__(self):
        pass

    def cadastro_pessoal(self):
        os.system("cls")
        print("---Cadastro Pessoal---\n")
        while True:
            self.nome_cadastro = input("Digite seu nome: ")
            if self.nome_cadastro.replace(" ","").isalpha():
                break
            else:
                print("\nDigite apenas letras!\n")
        while True:
            os.system("cls")
            print("---Cadastro Pessoal---\n")
            self.nome_cadastro = self.nome_cadastro.title()
            print(f"Nome digitado: {self.nome_cadastro}")
            verify = input("Seu nome está correto?(S/N)\n")
            verify = verify.upper()
            if verify == "S":
                os.system("cls")
                print("---Cadastro Pessoal---\n")
                break
            else:
                os.system("cls")
                while True:             
                    print("---Cadastro Pessoal---\n")
                    self.nome_cadastro = input("Digite seu nome: ")
                    if self.nome_cadastro.replace(" ","").isalpha():
                        break
                    else:
                        os.system("cls")
                        print("\nDigite apenas letras!\n")
        
        while True:
            while True:
                try:
                    self.__senha = int(input("Digite sua senha (apenas números): "))
                    break
                except ValueError:
                    os.system("cls")
                    print("---Cadastro Pessoal---\n")
                    print("Sua senha deve conter apenas números!\n")
            while True:
                try:
                    self.__senha2 = int(input("Digite sua senha novamente: "))
                    break
                except ValueError:
                    os.system("cls")
                    print("---Cadastro Pessoal---\n")
                    print("Sua senha deve conter apenas números!\n")
            if self.__senha == self.__senha2:
                os.system("cls")
                print("---Cadastro Pessoal---\n")
                break
            else:
                os.system("cls")
                print("---Cadastro Pessoal---\n")
                (print("Senhas não se coincidem, digite sua senha novamente!\n"))

        self.matricula = input("Digite sua matrícula: ")
        while True:
            os.system("cls")
            print("---Cadastro Pessoal---\n")
            print(f"Matrícula digitado: {self.matricula}")
            verify = input("\nSua matrícula está correta?(S/N)")
            verify = verify.upper()
            if verify == "S":
                os.system("cls")
                print("---Cadastro Pessoal---\n")
                break
            else:
                os.system("cls")
                print("---Cadastro Pessoal---\n")
                self.matricula = input("Digite sua matrícula novamente: ")

        while True:
            try:
                self.__telefone = int(input("Digite seu telefone: "))
                break
            except ValueError:
                os.system("cls")
                print("Digite apenas números!\n")
        while True:
            os.system("cls")
            print("---Cadastro Pessoal---\n")
            print(f"Telefone digitado: {self.__telefone}\n")
            verify = input("Seu telefone está correto? (S/N)\n")
            verify = verify.upper()
            if verify == "S":
                os.system("cls")
                print("---Cadastro Pessoal---\n")
                break
            else:
                print("---Cadastro Pessoal---\n")
                self.__telefone = input("Digite seu telefone novamente: ")

        self.__email = input("Digite seu email: ")
        while True:
            os.system("cls")
            print("---Cadastro Pessoal---\n")
            self.__email.replace(" ","")
            if not self.__email.endswith("@gmail.com\n"):
                self.__email += "@gmail.com"
            print(f"Email digitado: {self.__email}")
            verify = input("Seu email está correto? (S/N)")
            verify = verify.upper()
            if verify == "S":
                os.system("cls")
                print("---Cadastro Pessoal---\n")
                break
            else:
                self.__email = input("Digite seu email novamente: ")

        self.__endereco_p = input("Digite seu endereço: ")
        while True:
            os.system("cls")
            print("---Cadastro Pessoal---\n")
            print(f"Endereço digitado: {self.__endereco_p}")
            verify = input("Seu endereço está correto? (S/N)\n")
            verify = verify.upper()
            if verify == "S":
                os.system("cls")
                break
            else:
                os.system("cls")
                print("---Cadastro Pessoal---\n")
                self.__endereco_p = input("Digite seu endereço novamente: ")

    
    def cadastro_armas(self):
        os.system("cls")
        print("---Cadastro de armas---\n")

        self.tipo = input("Digite o tipo da arma: ")
        while True:
            os.system("cls")
            print(f"Tipo de arma digitado: {self.tipo}")
            verify = input("\nTipo de arma está correto? (S/N)\n")
            verify = verify.upper()
            if verify == "S":
                os.system("cls")
                print("---Cadastro de armas---\n")
                break
            else:
                self.tipo = input("\nDigite o tipo de arma novamente: ")


        self.__serial_number = input("Digite o número de série da arma: ")
        while True:
            os.system("cls")
            print(f"Número de série digitado: {self.__serial_number}")
            verify = input("\nNúmero de série está correto? (S/N)\n")
            verify = verify.upper()
            if verify == "S":
                os.system("cls")
                print("---Cadastro de armas---\n")
                break
            else:
                self.tipo = input("\nDigite o número de série novamente: ")

        self.calibre = input("Digite o calibre da arma: ")
        while True:
            os.system("cls")
            print(f"Calibre digitado: {self.calibre}")
            verify = input("\nCalibre está correto? (S/N)\n")
            verify = verify.upper()
            if verify == "S":
                os.system("cls")
                print("---Cadastro de armas---\n")
                break
            else:
                self.tipo = input("\nDigite o calibre novamente: ")

        while True:
            try:
                self.valor_arma = float(input("Digite o valor da arma: "))
                break
            except ValueError:
                print("Digite apenas números!")
        
        while True:
            print("---Cadastro de armas---\n")
            self.fabricacao = input("Digite a data de fabricação da arma (DD/MM/AA): ")
            self.fabricacao = self.fabricacao.replace(" ","")
            if not len(self.fabricacao) == 8:
                print("Digite data em formato dia, mes e ano (DD/MM/AAAA) sem a /")
                os.system("cls")                
            else:
                self.fabricacao = f"{self.fabricacao[:2]}/{self.fabricacao[2:4]}/{self.fabricacao[4:]}"
                os.system("cls")
                print("---Cadastro Cliente---\n")
                break

        self.marca = input("Digite a marca da arma: ")
        while True:
            os.system("cls")
            print(f"Marca da arma digitado: {self.marca}")
            verify = input("\nA marca da arma está correto? (S/N)\n")
            verify = verify.upper()
            if verify == "S":
                os.system("cls")
                print("---Cadastro de armas---\n")
                break
            else:
                self.tipo = input("\nDigite a marca da arma novamente: ")

    def cadastro_cliente(self):
        os.system("cls")
        while True:
            print("---Cadastro Cliente---\n")
            self.__nome_cliente = input("Digite seu nome: ")
            if self.__nome_cliente.replace(" ","").isalpha():
                break
            else:
                print("\nDigite apenas letras!\n")
        while True:
            os.system("cls")
            print("---Cadastro Cliente---\n")
            self.__nome_cliente = self.__nome_cliente.title()
            print(f"Nome digitado: {self.__nome_cliente}")
            verify = input("Seu nome está correto?(S/N)\n")
            verify = verify.upper()
            if verify == "S":
                os.system("cls")
                print("---Cadastro Cliente---\n")
                break
            else:
                os.system("cls")
                while True:                  
                    print("---Cadastro Cliente---\n")
                    self.__nome_cliente = input("Digite seu nome: ")
                    if self.__nome_cliente.replace(" ","").isalpha():
                        print("---Cadastro Cliente---\n")
                        break
                    else:
                        os.system("cls")
                        print("\nDigite apenas letras!\n")

        while True:
            try:
                self.__cpf = int(input("Digite seu CPF (apenas números): "))
                print("---Cadastro Cliente---\n")
                break
            except ValueError:
                print("Digite apenas números!")
        while True: 
            print(f"CPF digitado: {self.__cpf}")
            verify = input("Seu CPF está correto?(S/N)\n")
            verify = verify.upper()
            if verify == "S":
                os.system("cls")
                print("---Cadastro Cliente---\n")
                break
            else:
                self.__cpf = int(input("Digite seu CPF novamente: "))
                os.system("cls")

        while True:
            self.__data_nasc = input("Digite a data de nascimento (DD/MM/AAAA) a /: ")
            self.__data_nasc = self.__data_nasc.replace(" ","")
            if not len(self.__data_nasc) == 8:
                print("Digite data em formato dia, mes e ano (DD/MM/AAAA) sem a /")
            else:
                self.__data_nasc = f"{self.__data_nasc[:2]}/{self.__data_nasc[2:4]}/{self.__data_nasc[4:]}"
                os.system("cls")
                print("---Cadastro Cliente---\n")
                break

        while True: 
            self.__sexo = input("Digite seu sexo (M/F): ")
            self.__sexo.upper()
            if self.__sexo == "M" or self.__sexo == "F":
                break
            else:
                print("Digite M or F apenas.\n")

        self.__endereco_c = input("Digite seu endereço: ")

        while True:
            os.system("cls")
            print("---Cadastro Pessoal---\n")
            while True:
                try:
                    self.__salario = float(input("Digite seu salário: "))
                    break
                except ValueError:
                    print("Digite apenas números!")

            os.system("cls")
            print("---Cadastro Pessoal---\n")
            print(f"Matrícula digitado: {self.matricula}")
            verify = input("\nSeu salário está correto?(S/N)")
            verify = verify.upper()
            if verify == "S":
                os.system("cls")
                print("---Cadastro Pessoal---\n")
                break
            else:
                os.system("cls")
                print("---Cadastro Pessoal---\n")
                self.matricula = input("Digite seu salário novamente: ")



    def relatorio(self):
        while True:
            os.system("cls")
            try:
                menu_r = int(input("1 - Relatório Pessoal\n2 - Relatório da arma\n3 - Relatório Cliente"))
                break
            except ValueError:
                print("Digite apenas números!")

            if menu_r == 1:
                os.system("cls")
                print(f"=== Relatório Pessoal ===\n\nNome: {self.nome_cadastro}\nSenha: {self.__senha}\nMatrícula: {self.matricula}\nTelefone: {self.__telefone}\nEmail: {self.__email}\nEndereço: {self.__endereco_p}\n")
            elif menu_r == 2:
                os.system("cls")
                print(f"===Relatório da Arma===\n\nTipo de arma: {self.tipo}\nNúmero de série: {self.__serial_number}\nCalibre da arma: {self.calibre}\nValor da arma: R${self.valor_arma}\nData de fabricação da arma: {self.fabricacao}\nMarca da arma: {self.marca}\n")
            elif menu_r == 3:
                os.system("cls")
                print(f"===Relatório Cliente===\n\nNome: {self.__nome_cliente}\nCPF: {self.__cpf}\nData de nascimento: {self.__data_nasc}\nSexo: {self.__sexo}\nEndereço: {self.__endereco_c}\nSalário: R${self.__salario}\n")
            else:
                print("\nDigite um número válido!")