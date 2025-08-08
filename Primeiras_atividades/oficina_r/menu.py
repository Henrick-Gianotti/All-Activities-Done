from cadastro import *
from relatorio import *
from serviço import *
import time

register=cadastro_geral()

def main_menu():

    while True:
        menu=input("\n____Menu____\n1 - Cadastrar Cliente\n2 - Cadastrar Serviços\n3 - Ordem de Serviço\n4 - Imprimir Relatorio\n0 - Sair\n")
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
            while True:
                menu_service=input("____Menu____\n1 - Cadastrar Serivço\n2 - Alterar Serviço\n3 - Excluir Serviço\n0 - Voltar para o menu anterior")
                if menu_service == "1":
                    cadastro_serviço()

                elif menu_service == "2":
                    pass

                elif menu_service == "3":
                    cadastro_service_del()
                
                elif menu_service == "0":
                    os.system('cls')
                    break
                else:
                    os.system("cls")
                    print("\nPor favor, digite um número válido.\n")
                    continue

        elif menu == "3":
            while True:
                menu_OS = input("1 - Visualizar Ordem de Serviço\n0 - Voltar para o menu anterior")
                if menu_OS == "1":
                    pass
                elif menu_OS == "0":
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("\nPor favor, digite um número válido.\n")
                    continue

        elif menu == "4":
            report()

        elif menu == "0":
            print("Desligando...")
            time.sleep(3)
            os.system("cls")
            break
        else:
            os.system("cls")
            print("\nPor favor, digite um número válido.\n")
            continue