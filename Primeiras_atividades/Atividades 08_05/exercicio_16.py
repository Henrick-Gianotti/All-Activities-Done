lata=1
areat=float(input("Quantos m² será pintado?\n"))
litros=areat/3

while litros>18:
    litros=litros-18
    lata+=1
valor=lata*80
print("Será comprado",lata, "lata(s) no valor de R$%.2f"%valor)