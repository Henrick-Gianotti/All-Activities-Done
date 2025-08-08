from banco_dados import *

class cadastro():
    def __init__(self):
        pass

    def cadastro_f_cliente(self):
        while True:
            self.nome_cliente = input("Digite o nome: ").title()
            if self.nome_cliente.replace(" ","").isalpha():
                break
            else:
                print("Digite apenas letras!")

        self.idade_cliente = int(input("Digite a idade: "))
        self.cpf_client = int(input("Digite o cpf: "))
        self.telefone = int(input("Digite o telefone: "))
        self.veiculo_cliente = input("Tipo de veículo: ")
        self.veiculo_placa = input("Placa do veículo: ")
        self.veiculo_ano = int(input("Ano do Veículo: "))
        self.veiculo_defeito = input("Descreva o defeito: ")

        os.system('cls')
        return cadastro_banco(self.nome_cliente, self.idade_cliente,self.cpf_client, self.telefone, self.veiculo_cliente, self.veiculo_defeito)

    def cadastro_alt(self):
        while True:
            try:
                alt_quest_cpf = int(input("Qual CPF do cliente para alterar?\n"))
            except ValueError:
                print("Digite apenas números!")
                continue

            if alt_quest_cpf in cadastro_client:
                alt_client = cadastro_client[alt_quest_cpf]
                print(f"Cliente: {alt_client}")
                alt_quest_cat = input("\nDigite o nome do campo que irá atualizar: ")

                while True:
                    if alt_quest_cat == "cpf":
                        try:
                            new_cpf = int(input("Digite o novo CPF: "))
                        except ValueError:
                            print("Digite apenas números!")
                            continue
                        if new_cpf in cadastro_client:
                            print("O CPF já está cadastrado!")
                            continue
                        cadastro_client[new_cpf] = cadastro_client.pop(alt_quest_cpf)
                        print(f"O CPF do cliente foi alterado com sucesso: {cadastro_client[new_cpf]}")
                        break

                    elif alt_quest_cat in cadastro_client[alt_quest_cpf]:
                        new_data = input("Digite a nova informação: ")
                        cadastro_client[alt_quest_cpf][alt_quest_cat] = new_data
                        print(f"Cliente atualizado: {cadastro_client[alt_quest_cpf]}")
                        break

                    else:
                        print("Campo não encontrado")
                        alt_quest_cat = input("\nDigite o campo novamente: ")
                        continue
                break
            else:
                print("Cliente não encontrado")
                try:
                    alt_quest_cpf = int(input("Digite o cpf novamente: "))
                except ValueError:
                    print("Digite apenas números")
                    continue
                continue



    def cadastro_del(self):
        while True:
            cpf_cliente_del = input("Digite o nome do cliente que deseja remover: ")
            if cpf_cliente_del in cadastro_client:
                del cadastro_client[cpf_cliente_del]
                print(f"\nO registro do cliente {cpf_cliente_del} foi removido com sucesso")
                break
            else:
                print(f"\nNão foi encontrado nenhum registro do cliente {cpf_cliente_del}")
        
            
    

'''
    def peça(self):
        self.nome_peça = input("Digite o nome da peça: ")
        self.tipo_peça = input("Digite o tipo de peça: ")
        self.modelo = input("Digite o modelo da peça: ")
        return self.nome_peça, self.tipo_peça, self.modelo
    
    def orçamento(self):
        while True:
            try:
                self.preço = float(input("Valor do preço: "))
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número válido.")

        self.desc_valid = input("Possui desconto? (sim/nao)\n")
        if self.desc_valid == 'sim':
            while True:
                try:
                    self.desconto = float(input("Digite o valor do desconto: "))
                    break
                except ValueError:
                    print("Valor inválido. Por favor, digite um número.")
            self.preço = self.preço * 1.05 - self.desconto
        else:
            self.preço = self.preço * 1.05

        return self.preço
'''

'''
workshop=oficina_mec()
# call é atribuido o return da funçao, pode ser utilizado para colocar em uma lista
call=workshop.orçamento()
# posso printar direto caso nao queira colocar em uma lista
print(workshop.orçamento())
'''