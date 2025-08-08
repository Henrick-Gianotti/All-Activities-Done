num1=float(input("Insira o primeiro número\n"))
num2=float(input("Insira o segundo número\n"))

if num1>num2:
    print("O maior número digitado é %.0f"%num1)
elif num2>num1:
    print("O maior número digitado é %.0f"%num2)
else:
    print("Os dois números são iguais")