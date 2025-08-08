from fabrica import *

call = fabrica_armas()

def main_menu():
    while True:        
        menu = int(input("---Menu---\n1 - Cadastrar Pessoal\n2 - Cadastrar Arma\n3 - Cadastrar Cliente\n4 - Relatório\n0 - Sair\n"))
        if menu == 1:
            call.cadastro_pessoal()
            os.system("cls")
        elif menu == 2:
            call.cadastro_armas()
            os.system("cls")
        elif menu == 3:
            call.cadastro_cliente()
            os.system("cls")
        elif menu == 4:
            os.system("cls")
            call.relatorio()
        elif menu == 0:
            break
        else:
            print("\nDigite um número válido do menu!")
            os.system("cls")

main_menu()