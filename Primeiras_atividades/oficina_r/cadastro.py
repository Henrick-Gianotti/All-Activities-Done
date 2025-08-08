from banco_dados import *
import os

class cadastro_geral():    
    def __init__(self):
        pass
    
    def cadastro_f_cliente(self):
        while True:
            self.nome_cliente = input("Digite o nome: ").title()
            if self.nome_cliente.replace(" ","").isalpha():
                break
            else:
                print("Digite apenas letras!")
        while True:
            try:
                self.idade_cliente = int(input("Digite a idade: "))
                break
            except ValueError:
                print("Digite apenas números!")
                continue

        while True:
            self.cpf_client = input("Digite o cpf: ")  
            
            while True:
                if self.cpf_client.isdigit() and len(self.cpf_client) == 11:
                    break
                else:
                    self.cpf_client = input("Formato de CPF inválido! Digite novamente: ")

            if self.cpf_client in register:
                print(f"CPF {self.cpf_client} já cadastrado! Não pode cadastrar com o mesmo cpf.")
            else:
                break
            
        
        while True:
            try:
                self.veiculo_placa = int(input("Digite a placa do veículo: "))
                break
            except ValueError:
                print("Digite apenas números!")
                continue
        while True:
            try:
                self.telefone = int(input("Digite o telefone: "))
                break
            except ValueError:
                print("Digite apenas números!")
                continue
        while True:
            try:        
                self.veiculo_placa = int(input("Digite a placa do veículo: "))
                break
            except ValueError:
                print("Digite apenas números!")
                continue
        while True:
            try:
                self.veiculo_ano = int(input("Ano do Veículo: "))
                break
            except ValueError:
                print("Digite apenas números!")
                continue
        while True:
            self.chassi = input("Digite o chassi do carro: ")
            end_loop=input("O chassi do carro está correto? (sim/nao)\n")
            if end_loop == "sim":
                break
            elif end_loop == "nao":
                continue
            else:
                print("Digite sim ou nao!")

        os.system('cls')
        return banco_clientes(self.nome_cliente, self.idade_cliente, self.cpf_client, self.telefone, self.chassi, self.veiculo_placa, self.veiculo_ano)

    def cadastro_alt(self):
        
        while True:
            try:
                alt_quest_cpf = input("Digite o CPF do cliente ou 0 para voltar para o menu\n")
                
                if not register[alt_quest_cpf]:
                    print("CPF inválido! Por favor, digite um CPF válido.")
                    continue

                if alt_quest_cpf not in register:
                    print("CPF não encontrado")
                    continue

                alt_client = register[alt_quest_cpf]
                os.system("cls")
                print(f"Cliente: {alt_client['info_cliente']}")
                print("Campos disponíveis para alteração:")

                for key in alt_client['info_cliente'].keys():
                    print(f"  - {key.capitalize()}")
                alt_quest_cat = input("\nDigite o nome do campo que irá atualizar: ")

                if alt_quest_cat not in alt_client['info_cliente']:
                    print("Campo não encontrado")
                    continue

                new_data = input(f"Digite a nova informação para {alt_quest_cat}: ")
                alt_client['info_cliente'][alt_quest_cat] = new_data
                print(f"Campo {alt_quest_cat} atualizado com sucesso!")
                while True:
                    another_modification = input("Deseja alterar outro campo? (sim/nao): ")
                    if another_modification == "sim":
                        alt_quest_cat = input("Digite o campo que deseja alterar: ")
                        break
                    elif another_modification == "nao":
                        print("Alterações salvas com sucesso!")
                        break
                    else:
                        print("Digite sim ou nao!")
            except Exception as e:
                print(f"Erro: {e}")


    def cadastro_del(self):
        while True:
            cpf_cliente_del = input("Digite o CPF do cliente que deseja remover ou 0 para voltar ao menu anterior\n")
            if cpf_cliente_del in register:
                del register[cpf_cliente_del]
                print(f"\nO registro do cliente {cpf_cliente_del} foi removido com sucesso")
                break
            elif cpf_cliente_del == "0":
                break
            else:
                print(f"\nNão foi encontrado nenhum registro do cliente {cpf_cliente_del}")
