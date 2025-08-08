'''1 Faça um programa que peça um numero e então mostre a mensagem O número informado foi [numero]'''

num = float(input("Insira um número: "))
print("O número informado foi %.1f"% num)

'''2 Faça um programa que mostre a mensagem 'alo mundo' na tela'''

print("alo mundo")

'''3 Faça um programa que peça dois número e imprima a soma'''

num1=int(input("Insira um número\n"))
num2=int(input("Insira outro número\n"))
total=num1+num2
print("A soma dos números deu:",total)

'''4 Faça um programa que peça 4 notas bimestrais e mostre a média'''

nota1=float(input("Insira a primeira nota "))
nota2=float(input("Insira a segunda nota "))
nota3=float(input("Insira a terceira nota "))
nota4=float(input("Insira a quarta nota "))
media=(nota1+nota2+nota3+nota4)/4
print("Média do aluno é %2.1f"%media)

'''5 Faça um programa que converta metros para centímetros'''

metro=float(input("Insira o valor de metros "))
cm=metro*100
print("O valor de metros convertido em cm deu: %.1f"%cm)

'''6 Faça um programa que peça o raio de um círculo, calcule e mostre sua área'''

r=float(input("Insira o valor de raio "))
area=3.14*r**2
print("O valor da área do círculo é %.1fm"%area)

'''7 Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro dessta área para o usuário'''

aresta=float(input("Insira o valor de aresta "))
vertice=float(input("Insira o valor do vértice "))
area=aresta*vertice
area=area**2
print("O valor da área ao quadrado deu %.1f"%area)

'''8 Faça um programa que pergunte quanto voce ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês'''
#gph=ganho por hora; ht=horas trabalhadas
gph=float(input("Quanto você ganha por hora?\n"))
ht=float(input("Quantas horas você trabalha ao mês?\n"))
salario=gph*ht
print("Seu salário mensal é de %.2f"%salario)

'''9  '''
fah=float(input("Insira o valor em Fahrenheit"))
celsius = 5 * ((fah-32)/9)
print("Valor do fahrenheit convertido em celsius deu: %.2f"%celsius)

'''10'''
numint1=int(input("Insira um número inteiro\n"))
numint2=int(input("Insira outro número inteiro\n"))
numreal=float(input("Insira um número real\n"))
print(numint1,numint2,numreal)

'''11'''
primeiro=float(input("Insira o primeiro valor"))
segundo=float(input("Insira o segundo valor"))
terceiro=float(input("Insira o terceiro valor"))
letterA=(primeiro*2)/segundo
letterB=(primeiro*3)+(terceiro)
letterC=terceiro**3

'''12'''
# altura=float(input("Digite sua altura: "))
# pesoideal=(72.7*peso)-58
# print("Seu peso ideial é %.2f"%pesoideal)

'''13'''
#h=altura
# h=float(input("Digite sua altura"))
# sexo=input("Qual seu sexo?\n")

# if sexo == 'm':
#     pesoideal=(72.7*h)-58
#     print("Seu peso ideal é %.2f"%pesoideal)
# elif sexo == 'f':
#     pesoideal=(62.1*h)-44.7
#     print("Seu peso ideal é %.2f"%pesoideal)
# else:
#     print("Sexo inválido")

'''14'''
# quiloexcedido=float(input("Insira quantos kilos deu a pesca\n"))

# if quiloexcedido >= 51:
#     pesoexcedido=(quiloexcedido-50)
#     valorexcedido=(quiloexcedido-50)*4
#     print("O peso excedeu 50 kilos, dando %.0fkg a mais."%pesoexcedido)
#     print("A multa será de R$%.2f reais."%valorexcedido)
# else:
#     print("Sem peso excedente.")

'''15'''
#gph=ganho por hora;
gph=float(input("Quanto você ganha por hora?\n"))
#ht=horas trabalhadas;
ht=float(input("Quantas horas você trabalha ao mês?\n"))

imp=1.11
inss=1.08
sindicato=1.05
salariobruto=(gph*ht)
desc_imp=salariobruto*imp-salariobruto
desc_inss=salariobruto*inss-salariobruto
desc_sind=salariobruto*sindicato-salariobruto
salarioliquido=salariobruto-desc_imp-desc_inss-desc_sind

print("Seu salário bruto mensal é de %.2f"%salariobruto)
print("Você pagou R$%.2f em imposto"%desc_imp)
print("Você pagou R$%.2f em INSS"%desc_inss)
print("Você pagou R$%.2f para o sindicato"%desc_sind)

print("Seu salário líquido mensal é de %.2f"%salarioliquido)

'''16'''
lata=1
areat=float(input("Quantos m² será pintado?\n"))
litros=areat/3

while litros>18:
    litros=litros-18
    lata+=1
valor=lata*80
print("Será comprado",lata, "lata(s) no valor de R$%.2f"%valor)


'''17'''
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


'''18'''
tamanho=float(input("Qual o tamanho do arquivo em GB?\n"))
velocidade=float(input("QUal a velocidade da sua internet em Mbps?\n"))
convert=tamanho*1000
tempo=(convert/velocidade)/60
print("O tempo necessário para baixar o arquivo é %.1f minutos"%tempo)


'''19'''
num1=float(input("Insira o primeiro número\n"))
num2=float(input("Insira o segundo número\n"))

if num1>num2:
    print("O maior número digitado é %.0f"%num1)
elif num2>num1:
    print("O maior número digitado é %.0f"%num2)
else:
    print("Os números são iguais")


'''20'''
num=float(input("Insira um número\n"))
if num>0:
    print("O número digitado é positivo")
elif num<0:
    print("O número digitado é negativo")
else:
    print("O número digitado é zero (neutro)")