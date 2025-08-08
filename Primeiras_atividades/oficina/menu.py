from oficina import *
from report import *
import time

register=cadastro()

def menu():

    while True:
        menu=input("\n____Menu____\nManda a braba\n1 - Cadastrar Cliente\n2 - Cadastrar Serviços\n3 - Visualizar Ordem de Serviço\n4 - Imprimir Relatorio\n0 - Sair\n")
        if menu == "1":
            os.system('cls')
            while True:
                menu_register=input("\n____Menu____\n1 - Cadastrar Cliente\n2 - Alterar Cadastro\n3 - Excluir Cadastro\n0 - Voltar para o menu anterior\n")
                if menu_register == "1":
                    print(register.cadastro_f_cliente())

                elif menu_register == "2":
                    register.cadastro_alt()

                elif menu_register == "3":
                    register.cadastro_del()
                
                elif menu_register == "0":
                    os.system('cls')
                    break
                else:
                    os.system("cls")
                    print("\nPor favor, digite um número válido.\n")
                    continue
            
        elif menu == "2":
            pass
        
        elif menu == "3":
            pass
        # ordem de serviço: será um relatorio informando apenas os serviços, desde cadastrar/mostrar o que foi feito 

        elif menu == "4":
            report()

    # perigoso demais para utilizar
            # for cliente,dados in cadastro_client.items():
            #     print(f"Cliente: {cliente}\nIdade: {dados['Idade']}\nTelefone: {dados['Telefone']}\nVeiculo: {dados['Veiculo']}\nDefeito: {dados['Defeito']}\n")

        elif menu == "0":
            print("Desligando...")
            time.sleep(3)
            os.system("cls")
            break
        else:
            os.system("cls")
            print("\nPor favor, digite um número válido.\n")
            continue