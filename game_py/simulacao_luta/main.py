from duelo import *

call = duel()

menu = 10

while True:
    menu = int(input(" 1-Começar a luta\n 2-Sair da simulação\n"))
    if (menu == 1):
        os.system('cls')
        call.start()
    elif (menu == 2):
        os.system('cls')
        print("encerrando a simulação...")
        time.sleep(2)
        break
    else:
        print("Digita 1 ou 2 cara")
        menu = int(input("1-Começar a luta\n 2-Sair da simulação\n"))