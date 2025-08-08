tamanho=float(input("Qual o tamanho do arquivo em GB?\n"))
velocidade=float(input("QUal a velocidade da sua internet em Mbps?\n"))
convert=tamanho*1000
tempo=(convert/velocidade)/60
print("O tempo necessário para baixar o arquivo é %.1f minutos"%tempo)