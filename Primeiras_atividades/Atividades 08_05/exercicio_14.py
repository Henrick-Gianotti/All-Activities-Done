quiloexcedido=float(input("Insira quantos kilos deu a pesca\n"))

if quiloexcedido >= 51:
    pesoexcedido=(quiloexcedido-50)
    valorexcedido=(quiloexcedido-50)*4
    print("O peso excedeu 50 kilos, dando %.0fkg a mais."%pesoexcedido)
    print("A multa será de R$%.2f reais."%valorexcedido)
else:
    print("Sem peso excedente.")