def only_lata():
    import math
    lata=1

    areat=float(input("Quantos m² será pintado?\n"))
    litros=areat/6
    # 10% de folga
    litros=litros*1.1
    litros=math.ceil(litros)

    while litros>18:
        litros=litros-18
        lata+=1
    valor=lata*80
    print("Será comprado",lata, "lata(s) no valor de R$%.2f"%valor)

def only_galao():
    import math
    galao=1

    areat=float(input("Quantos m² será pintado?\n"))
    litros=areat/6
    # 10% de folga
    litros=litros*1.1
    litros=litros*1.1
    litros=math.ceil(litros)

    while litros>3.6:
        litros=litros-3.6
        galao+=1
    valor=galao*25
    print("Será comprado",galao,"galão(ões) no valor de R$%.2f"%valor)

def lata_galao():
    import math
    galao=1
    lata=1
    
    areat=float(input("Quantos m² será pintado?\n"))
    litros=areat/6
    # 10% de folga
    litros=litros*1.1
    litros=math.ceil(litros)
    while litros>=18:
        litros=litros-18
        lata+=1

    if litros > 10.8:
        lata+=1
    else:
        while litros>=3.6:
            litros=litros-3.6
            galao+=1

        valor=lata*80 + galao*25
        print("Será comprado",lata,"lata(s) e",galao,"galão(ões) no valor de R$%.2f"%valor)

chamar=input("(1)Somente latas\n(2)Somente galão\n(3)Latas e galões\n")

if chamar == '1':
   ex1=only_lata()
elif chamar == '2':
    ex2=only_galao()
elif chamar == '3':
    ex3=lata_galao()
else:
    print("Número inválido")