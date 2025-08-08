from banco_dados import *

def report():
    while True:
        type = int(input("Qual o cpf do cliente?\n"))
        os.system("cls")
        if type in cadastro_client:
            for cpf, dados in cadastro_client[type].items():                
                print(f"{cpf}: {dados}")
            break
        else:
            print("CPF não encontrado")
        