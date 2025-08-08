from banco_dados import *

def report():

    while True:

        cpf_input = (input("Digite o cpf do cliente para visualizar o relatório ou 0 para voltar ao menu anterior\n"))
        os.system("cls")
  
        if cpf_input in register:
            print("cpf encontrado")
            dados = register[cpf_input]
            print("Informações do Cliente:")

            for key, value in dados["info_cliente"].items():
                print(f"  {key.capitalize()}: {value}")
            print("Ordem de Serviço:")

            if "serviços" in dados:
                for service in dados["serviços"]:
                    for key, value in service.items():
                        print(f"  {key}:")
                        for i, z in value.items():
                            print(f"  {i.capitalize()}: {z}")
        elif cpf_input == "0":
            break
        else:
            print("CPF não encontrado\n")
            

