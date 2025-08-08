#h=altura
h=float(input("Digite sua altura: "))
sexo=input("Qual seu sexo?\nDigite m para masculino e f para feminino: ")

if sexo == 'm':
    pesoideal=(72.7*h)-58
    print("Seu peso ideal é %.2f"%pesoideal)
elif sexo == 'f':
    pesoideal=(62.1*h)-44.7
    print("Seu peso ideal é %.2f"%pesoideal)
else:
    print("Sexo inválido")