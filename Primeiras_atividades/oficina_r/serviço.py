from banco_dados import *

def cadastro_serviço():
    os.system("cls")
    while True:
        cpf_cliente = input("Digite o cpf do cliente: ")

        if cpf_cliente in register:
            service = input("--Descreva o serviço--\n")
            peça = input("Nome da peça: ")
            while True:
                try:
                    orçamento = int(input("Valor do serviço: "))
                    break
                except ValueError:
                    os.system("cls")
                    print("\nDigite apenas números!")
                    continue
            return banco_service(cpf_cliente, service, peça, orçamento)

        else:
            print("---CPF não cadastrado!---\n Não é possível cadastrar serviço sem um CPF cadastrado.")
            exit=input("\n\nPressione Enter para continuar ou 0 para voltar ao menu anterior")
            if exit == "0":
                break
            else:
                continue

def cadastro_service_del():
    while True:
        cpf_service_del = input("Digite o CPF do cliente que deseja remover ou 0 para voltar ao menu anterior\n")
        if cpf_service_del in register:
            del register[cpf_service_del]["serviços"]
            print(f"\nO registro de serviços do cliente {cpf_service_del} foi removido com sucesso")
            break
        elif cpf_service_del == "0":
            break
        else:
            print(f"\nNão foi encontrado nenhum registro de serviço do cliente {cpf_service_del}")

def cadastro_service_alt():

    end_loop=False
    back_menu="0"
    while True:
        if back_menu=="1":
            break
        alt_quest_cpf = input("Digite o CPF do cliente: ")
        while True:
            if alt_quest_cpf.isdigit():
                break
            else:
                print("Digite apenas números!")

        if alt_quest_cpf not in register:
            print("CPF não encontrado")
            alt_quest_cpf = input("Digite o cpf novamente: ")

            if alt_quest_cpf.isdigit():
                alt_quest_cpf = int(alt_quest_cpf)
            else:
                print("Digite apenas números!")
                continue

        alt_client = register[alt_quest_cpf]
        os.system("cls")
        print(f"Cliente: {alt_client['info_cliente']}")
        print("Serviços disponíveis para alteração:")

        if "serviços" in alt_client:
            for i, service in enumerate(alt_client["serviços"]):
                print(f"  - Serviço {i+1}: {service[list(service.keys())[0]]['serviço']}")
            alt_quest_service = input("\nDigite o número do serviço que irá atualizar: ")
            try:
                alt_quest_service = int(alt_quest_service)
                if alt_quest_service > 0 and alt_quest_service <= len(alt_client["serviços"]):
                    service_to_update = alt_client["serviços"][alt_quest_service-1]
                    print(f"Serviço {alt_quest_service}: {service_to_update[list(service_to_update.keys())[0]]['serviço']}")
                    print("Campos disponíveis para alteração:")
                    for key in service_to_update[list(service_to_update.keys())[0]].keys():
                        print(f"  - {key.capitalize()}")
                    alt_quest_field = input("\nDigite o campo que irá atualizar: ")

                    while True:
                        if alt_quest_field in service_to_update[list(service_to_update.keys())[0]]:
                            new_data = input(f"Digite a nova informação para {alt_quest_field}: ")
                            service_to_update[list(service_to_update.keys())[0]][alt_quest_field] = new_data
                            print(f"Campo {alt_quest_field} atualizado com sucesso!")
                            while True:
                                another_modification = input("Deseja alterar outro campo? (sim/nao): ")
                                if another_modification == "sim":
                                    alt_quest_field = input("Digite o campo que deseja alterar: ")
                                    break
                                elif another_modification == "nao":
                                    print("Alterações salvas com sucesso!")
                                    end_loop = True
                                    break
                                else:
                                    print("Digite sim ou nao!")
                            if end_loop == True:
                                back_menu="1"
                                break
                        else:
                            print("Campo não encontrado")
                            alt_quest_field = input("\nDigite o campo novamente: ")
                            continue
                else:
                    print("Serviço não encontrado")
                    alt_quest_service = input("Digite o número do serviço novamente: ")
            except ValueError:
                print("Digite um número válido!")
                continue
        else:
            print("Não há serviços cadastrados para este cliente.")
            back_menu="1"
            break

def valor_serviço():
    while True:
        cpf_cliente=input("Digite o cpf do cliente: ")
        if cpf_cliente in register:
            orcamento_total = 0
            for servico in register[cpf_cliente]["serviços"]:
                for i, z in servico.items():
                    orcamento_total += float(z["orçamento"])
            break
        else:
            print("---CPF não existe!---\nNão é possível calcular orçamento sem um CPF cadastrado.\n")
            continue