#Descriçao do aluno + média

nome=input("Insira o nome do aluno: ")
idade=int(input("Insira a idade do aluno: "))
sexo=input("Insira o sexo do aluno:")
nota1=float(input("Insira a primeira nota\n"))
nota2=float(input("Insira a segunda nota\n"))

media=(nota1+nota2)/2

print("O aluno",nome,"de",idade,"anos e sexo",sexo,"possui a média de:% 2.1f" % media)